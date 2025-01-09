# helpers.py

import random
import string

def generate_unique_slug(model_instance, field_name, value):
    """
    Generate a unique slug for a model instance based on a field value.
    If the slug already exists, append a random string to make it unique.
    """
    base_slug = value.replace(' ', '-').lower()  # Make the slug lowercased and replace spaces with hyphens
    slug = base_slug
    model_class = model_instance.__class__
    counter = 1
    
    # Check if the slug already exists
    while model_class.objects.filter(slug=slug).exists():
        # Append a random string to the slug if it exists
        slug = f"{base_slug}-{generate_random_string()}"
        counter += 1
        
    return slug

def generate_random_string(length=6):
    """Generate a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
