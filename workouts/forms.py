from django import forms
from .models import Type, Workout, Intensity


# Workout form class
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = [
            'title', 'type', 'description',
            'intensity', 'burned', 'image_url'
        ]

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        # make image_url fields optional
        self.fields['image_url'].required = False
        self.fields['type'].queryset = Type.objects.all()
        self.fields['intensity'].queryset = Intensity.objects.all()
