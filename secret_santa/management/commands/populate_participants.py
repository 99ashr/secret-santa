from django.core.management.base import BaseCommand
from secret_santa.models import Participant


class Command(BaseCommand):
    help = 'Populate the database with 34 hardcoded participants'

    def handle(self, *args, **options):
        # List of 34 participants
        participants = [
            'Aditya Razdan', 'Apoorbha Das', 'Ashish Kumar Saini', 'Athul Krishna P',
            'Chaitanya Machindra Ambekar', 'Drashti Maniyar', 'Himanshu', 'Kamlesh Gadhvi',
            'Karan Kumar Jena', 'Kattuparampil Jino Kuriakose', 'Khatib Hyder Khan', 'Kshitiz Chaurasia',
            'Nalin Raj J', 'Nikhil Anil Salunke', 'Nikita Vijay', 'Prathamesh Shukla',
            'Rituraj Choudhury', 'Saptarshi Das', 'Shishira Kanta Jena', 'Sumant Kumar',
            'Surendra Kumar', 'Tanmay Rajendra Tabhane', 'Vishnu Krishnan', 'Devansh Kumar',
            'Chandan', 'Mohit Alam', 'Ashish Guar', 'Ashutosh',
            'Rutuja', 'Ravi Siddarth', 'Patil Vijay', 'Aryaveer Ray',
            'Megna Shukla', 'Sahil Bambarde'
        ]
        
        # Check if participants already exist
        existing_count = Participant.objects.count()
        
        if existing_count >= 34:
            self.stdout.write(
                self.style.WARNING(f'Already have {existing_count} participants. Skipping.')
            )
            return
        
        # Create participants
        created_count = 0
        for name in participants:
            participant, created = Participant.objects.get_or_create(name=name)
            if created:
                created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} participants')
        )
