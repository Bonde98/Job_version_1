from django.core.exceptions import ValidationError

# Vérifie le mot est-ce qu'il y'a une lettre
class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot doit contenir une lettre', code='password_no_letter'
            )
     # Guide l'utilisateur, pour qu'il save comment passer la validation
    def get_help_text(self):
        return 'Le mot de passe doit contenir au moins une lettre majuscule ou minuscule'
