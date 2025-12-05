from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from .models import Participant, DrawMapping
import json


def index(request):
    """Admin page for generating draws"""
    draw_count = DrawMapping.objects.count()
    participant_count = Participant.objects.count()
    context = {
        'draw_count': draw_count,
        'participant_count': participant_count,
    }
    return render(request, 'secret_santa/admin.html', context)


def participant_page(request):
    """Participant page for entering token and revealing recipient"""
    return render(request, 'secret_santa/participant.html')


@require_http_methods(["POST"])
def generate_draw(request):
    """Generate Secret Santa draw using derangement algorithm"""
    try:
        # Delete existing draw if any
        DrawMapping.objects.all().delete()
        
        # Get all participants
        participants = list(Participant.objects.all().order_by('id'))
        
        if len(participants) < 2:
            return JsonResponse({
                'success': False,
                'message': 'Not enough participants for draw (minimum 2 required)'
            }, status=400)
        
        # Generate derangement
        recipients = DrawMapping.derangement_shuffle(participants)
        
        # Create mappings with tokens
        mappings = []
        for giver, recipient in zip(participants, recipients):
            token = DrawMapping.generate_token()
            
            # Ensure token is unique
            while DrawMapping.objects.filter(token=token).exists():
                token = DrawMapping.generate_token()
            
            mapping = DrawMapping.objects.create(
                token=token,
                giver=giver,
                recipient=recipient
            )
            mappings.append({
                'token': token,
                'giver': giver.name,
                'recipient': recipient.name
            })
        
        return JsonResponse({
            'success': True,
            'message': f'Draw generated successfully for {len(mappings)} participants',
            'count': len(mappings)
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error generating draw: {str(e)}'
        }, status=500)


@require_http_methods(["GET"])
def show_tokens(request):
    """Get all tokens and mappings for admin (without revealing recipients)"""
    try:
        mappings = DrawMapping.objects.all().select_related('giver', 'recipient')
        tokens_list = [
            {
                'token': m.token,
                'giver': m.giver.name,
                'created_at': m.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for m in mappings
        ]
        
        return JsonResponse({
            'success': True,
            'tokens': tokens_list,
            'total': len(tokens_list)
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error retrieving tokens: {str(e)}'
        }, status=500)


@require_http_methods(["POST"])
def clear_draw(request):
    """Clear all draw mappings"""
    try:
        count = DrawMapping.objects.count()
        DrawMapping.objects.all().delete()
        
        return JsonResponse({
            'success': True,
            'message': f'Cleared {count} draw mappings'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error clearing draw: {str(e)}'
        }, status=500)


@require_http_methods(["POST"])
def reveal_recipient(request):
    """Participant enters token to reveal recipient"""
    try:
        data = json.loads(request.body)
        token = data.get('token', '').strip().upper()
        
        if not token:
            return JsonResponse({
                'success': False,
                'message': 'Token is required'
            }, status=400)
        
        mapping = DrawMapping.objects.filter(token=token).first()
        
        if not mapping:
            return JsonResponse({
                'success': False,
                'message': 'Invalid token. Please check and try again.'
            }, status=404)
        
        # Mark as revealed
        if not mapping.is_revealed:
            mapping.is_revealed = True
            mapping.revealed_at = timezone.now()
            mapping.save()
        
        return JsonResponse({
            'success': True,
            'recipient': mapping.recipient.name,
            'message': f'Your Secret Santa recipient is: {mapping.recipient.name}! 🎄'
        })
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error revealing recipient: {str(e)}'
        }, status=500)
