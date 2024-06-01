# Image generator Project

## Steps to run the project

1. You need to have new openai account
2. Create new API KEY from the that and store in any parmanent environment variable for hiding the key and giving secure access.
3. Create one project environment variable
``` conda create -n imageGen python=3.8 -y ```
4. Install requiremments 
``` pip install -r requirements.txt ```
5. (Optionanl) Even after intalling openai latest version my code was giving verion issue hence I installed lower version of openai. Which is openai==0.28
6. Now run the generate_image.py
``` python genarate_image.py ```
7. It will give url of new genarated image as per the prompt.
8. But I got error as my openai account is more than 3 month old and hence free credit is expired already
![ [OpenAI Billing Limit reached] ](Billing_limit_Error.png)

9. Error while running the model
![ [OpenAI Billing Limit reached] ](billing_error.png)