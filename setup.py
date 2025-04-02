from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()
    
    setup(
        name='Crop_Recommendation Prediction Model',
        version='1.0.0',
        description='CropRecommendationPredictionModel',
        url='https://github.com/chandanc5525/Crop_Recommendation_Model',
        author= 'Chandan Chaudhari',)