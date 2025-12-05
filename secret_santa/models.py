from django.db import models
import secrets
import string


class Participant(models.Model):
    """Hardcoded list of participants"""
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
    
    def __str__(self):
        return self.name


class DrawMapping(models.Model):
    """Maps token to gift recipient and giver"""
    token = models.CharField(max_length=6, unique=True, db_index=True)
    giver = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='giving_tokens')
    recipient = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='receiving_tokens')
    is_revealed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    revealed_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Draw Mapping'
        verbose_name_plural = 'Draw Mappings'
    
    def __str__(self):
        return f"{self.token} - {self.giver.name} → {self.recipient.name}"
    
    @staticmethod
    def generate_token():
        """Generate a random 6-character alphanumeric token"""
        chars = string.ascii_uppercase + string.digits
        return ''.join(secrets.choice(chars) for _ in range(6))
    
    @staticmethod
    def derangement_shuffle(participants):
        """
        Create a derangement (no one gets themselves) using Fisher-Yates shuffle.
        Returns a list of recipient pairs matched with givers.
        Attempts up to 5000 iterations to find a valid derangement.
        """
        import random
        
        for _ in range(5000):
            recipients = participants.copy()
            random.shuffle(recipients)
            
            # Check if it's a valid derangement (no person is at same position as giver)
            if all(recipients[i] != participants[i] for i in range(len(participants))):
                return recipients
        
        # Fallback: If no perfect derangement found, swap first two elements
        # (This is a compromise for edge cases)
        recipients = participants.copy()
        random.shuffle(recipients)
        if recipients[0] == participants[0]:
            recipients[0], recipients[1] = recipients[1], recipients[0]
        return recipients
