# Atlas SmartEat - Diet Recommendation SaaS Application

<div align= "center" ><img src="AtlasFrontend/logo.png" width=300 />
</div>

## Overview

Atlas SmartEat is a cutting-edge SaaS web application designed to revolutionize the way individuals approach their dietary habits. Utilizing advanced machine learning algorithms, Generative AI and a user-friendly interface, this platform offers personalized diet recommendations and assistance to promote healthier lifestyle choices.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Architecture](#architecture)
- [Key Features and Services](#key-features-and-services)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)

## Problem Statement

In an era where health consciousness is paramount, many individuals struggle to find reliable, personalized dietary recommendations. The challenge lies in creating a system that not only understands diverse nutritional needs but also aligns with personal preferences and restrictions.

## Solution

Atlas SmartEat addresses this challenge by offering a content-based recommendation system. By analyzing individual user profiles, dietary preferences, and nutritional values, it provides tailored diet plans that align with personal health goals and dietary restrictions. Also, an Interactive chatbot based on generative AI to assist and guide the user for a healthier lifestyle.

## Architecture

### Backend

- **Machine Learning Model**: Implements a Nearest Neighbors algorithm to analyze and suggest dietary recommendations.
- **API Layer**: Built with FastAPI, it handles requests and serves recommendations based on user data.

### Frontend

- **User Interface**: Developed using Streamlit, offering an intuitive and responsive design.
- **Interaction Layer**: Allows users to input personal data, preferences, and receive customized diet plans.

### Model Development

The engine utilizes the Nearest Neighbors algorithm for its recommendations, specifically employing the brute-force algorithm using cosine similarity for its efficiency with small datasets. We utilized the extensive Food.com dataset from Kaggle, featuring over 500,000 recipes and 1.4 million reviews.

### Generative AI

With the help of Open AI API, We built an interactive chatbot thant answer the user all his diet and healthcare questions considering his health information.

### Deployment

- **Containerization**: Utilizes Docker for consistent deployment and scalability.
- **Cloud Integration**: Hosted on cloud platforms for high availability and performance.

## Technologies Used

- Python
- Scikit-Learn
- Open IA API
- FastAPI
- Streamlit
- Docker

## Getting Started

To start using Atlas SmartEat, follow these steps:

1. Clone the repository: `git clone https://github.com/hadryyassine/Atlas-SmartEat.git`
2. Run the application: `docker-compose up -d --build`
