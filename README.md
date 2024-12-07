# Pet Vibe

Pet Vibe is a user-friendly B2C platform designed for pet owners to explore and purchase high-quality pet products and services. From grooming services to essential pet products.

The platform also features a secure payment system powered by Stripe. Please note that this website is for educational purposes; do not enter personal credit/debit card details. Test card details provided by Stripe can be used, as documented [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [Pet Vibe](https://pet-vibe-368356973856.herokuapp.com/)

![Site Mockup](docs/readme_images/mockup.png)

- [User Experience (UX)](#user-experience--ux-)
    * [User Stories](#user-stories)
    * [Design](#design)
        + [Colour Scheme](#colour-scheme)
- [Agile Methodology](#agile-methodology)
- [Languages](#languages)
- [Deployment - Heroku](#deployment---heroku)
- [AWS Set Up](#aws-set-up)
- [Forking this repository](#forking-this-repository)
- [Cloning this repository](#cloning-this-repository)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)


## User Experience (UX)

Pet Vibe is designed with a user-centric approach, ensuring ease of navigation, clear functionality, and seamless engagement for shoppers, pet owners, and site administrators.

### User Stories

### EPIC | Browsing and Navigation
- As a shopper, I can view a list of products so that I can select a product to view.
- As a shopper, I can view product categories so that I can browse the type of products I'm interested in.
- As a site user, I can view a grooming services page so that I can see the types of services available and their prices.
- As a site user, I can access a contact page so that I can submit inquiries or feedback.

### EPIC | User Account and Profile

- As a site user, I can register an account so that I can have a personal profile and save my details.
- As a site user, I can log in or log out so that I can keep my account secure.
- As a site user, I can view my profile page so that I can see my saved information and history.

### EPIC | Purchasing

- As a shopper, I can add products to my shopping bag so that I can purchase multiple items together.
- As a shopper, I can view the contents so that I can see the total price of my shopping bag.
- As a shopper, I can change the quantity of items in my shopping bag so that I can adjust my order.
- As a shopper, I can securely enter my payment details so that I can complete my purchase.

### EPIC | Site Administration

- As a site owner, I can add, edit, or delete products through an interface so that I can maintain the site updated.
- As a store owner, I can approve or delete customer testimonials so that I can control what feedback is shown on the site.
- As a store owner, I can view customer inquiries submitted on the contact page so that I can respond to customer feedback or questions.

### EPIC | User Interaction

- As a site user, I can read testimonials left by other customers so that I can see their feedback on products and services.
- As a site user, I can submit a testimonial after purchasing a product or service so that I can provide feedback.
- As a site user, I can submit a contact form so that I can inquire about products or services.

## Agile Methodology
GitHub Projects was used to manage the development process of the Pet Vibe project, following an Agile approach. This ensured that the project was developed incrementally, with flexibility to adapt to changing requirements and priorities. The project board can be accessed [here](https://github.com/users/thiago-23/projects/15)

### Epics and User Stories

The development process was structured around the 5 main Epics, each representing a significant aspect of the project. These Epics were broken down into smaller, actionable User Stories, allowing for focused and efficient development

### Design

The site uses a warm, welcoming palette inspired by nature, including greens, browns, and neutral tones to evoke trust and comfort.

#### Colour Scheme

![Colour Scheme](docs/readme_images/colour_scheme.png)

### Header
![header](/docs/readme_images/features%20/header.png)

**Logo**

- Positioned at the top-left, linked to the home page, once click on the Pet Vibe logo it redirect to the home page for ease of navigation for the user.

**Navigation Bar**

- The Navigation bar includes links to key site areas like Products, Grooming, Testimonials and contact and it is visible at the top of every page.

**Search Bar**

![Search](/docs/readme_images/features%20/search.png)
- The search bar is prominently positioned above the navigation bar for easy access.
- Users can input keywords, and the search functionality dynamically scans product titles and descriptions, displaying matching results on the product listing page.
- On smaller screens, the search bar transforms into a compact search icon. Clicking this icon reveals the full search bar in a dropdown format.

**User Icon**

![Logged In](/docs/readme_images/features%20/user_logged.png)

- The User icon serves as a navigation link that opens a dropdown menu, providing quick access to account-related actions.
- For visitors who are not logged in, the dropdown includes links to "Register" and "Log In," enabling account creation or authentication.
- After successfully signing in, the dropdown menu dynamically updates, and replacing the "Register" and "Log In" options with a "Log Out" link for easy account management.
- Additionally, the "My Profile" option becomes available in the dropdown menu, allowing users to quickly access and manage their personal account details.

![AdminLogged In](/docs/readme_images/features%20/superuser_logged.png)

- When a superuser logs in, the User icon dropdown menu dynamically expands to include additional management functionalities tailored for administrative purposes.
- These options include: Product Management and Service Management.
- This expanded functionality ensures that superusers have full control over the platform's content and user interactions, enhancing operational efficiency.

**Bag Icon**

![bag](/docs/readme_images/features%20/bag_icon.png)

- The Bag Icon, positioned on the right side of the navigation bar beside the User icon, provides quick access to the user's shopping bag.
- When a product is added to the bag:
    - A badge displaying the total quantity of items is dynamically updated and the total appears at the button of the bag icon.
    - A toast notification is triggered in the top-right corner of the screen, confirming the addition of the item.
- The toast includes:
    - A brief snapshot of the bag contents.
    - The current total cost of the items in the bag.
    - This feature enhances the shopping experience by providing real-time feedback and a convenient overview of the user's selections, streamlining the process from browsing to checkout.

### Home Page

![Home page](/docs/readme_images/features%20/home_page.png)

- The Home Page of Pet Vibe greets users with a welcoming and engaging call-to-action section, designed to immediately capture attention and guide user interaction.

- The central message, **"Welcome to Pet Vibe! Making Pets Shine, because they're worth it!"**, sets the tone for the site, emphasizing care, quality, and dedication to pets.
- **Shop Now** Button: A prominently placed button encourages users to start exploring and purchasing products right away.
- **Grooming** Services: Another actionable link directs users to view and explore available grooming services and prices.
- This design ensures that the homepage serves as both a welcoming introduction to Pet Vibe and a functional starting point for users to quickly access the site's key offerings

### Footer

![footer](/docs/readme_images/features%20/footer.png)

- The footer is a consistent element located at the bottom of every page, providing users with easy access to additional features and navigation options.

- Features of the Footer:
    - Social Media Links: Direct links to Facebook, Instagram and Twitter allow users to connect with the platform's social media presence.
    - Newsletter Signup: A Mailchimp-powered subscription form enables users to enter their email address to subscribe to a monthly newsletter, keeping them updated on new products, services, and offers.
    - Quick Links Section: Provides convenient navigation to essential site pages like Contact Us and Privacy Policy.
- External Link Behavior: All external links are designed to open in a new tab, ensuring users remain engaged with the website while exploring additional content.

### User Account Pages

**Sign Up**

![Sign Up](/docs/readme_images/features%20/sign_up.png)

**Sign In**

![Sign Up](/docs/readme_images/features%20/sign_in.png)

**Log Out**

![Sign Up](/docs/readme_images/features%20/sign_out.png)

- Pet Vibe makes managing your account super simple and secure with Django Allauth powering the system. Here’s how it works:

- Sign Up, Log In, and Log Out: Creating an account is quick and easy. Once you're in, you can log in and out anytime you want without hassle.
- Clear Success Messages: Every time you log in or out, you’ll see a quick confirmation message so you know it worked.
- Email Verification: To keep everything secure, you’ll get an email when you sign up. Just click the link in that email to activate your account.
- Forgot Your Password? No Problem! If you ever forget your password, there’s a "Forgot Password" link on the login page. Just click it, and you’ll get an email to reset your password in no time.
- It’s all about making it easy for you to manage your account while keeping your info safe and secure. 😊

### Profile
**Delivery Details**

![Delivery Details](/docs/readme_images/features%20/delivery_info.png)

- The Delivery Details section in your profile keeps your delivery address and phone number saved securely, so you don’t have to type them out every time.
When you’re ready to place an order, your saved details will autofill the delivery form—making the checkout process quick and ease.

**Order History**

![Order History](/docs/readme_images/features%20/order_history.png)

- The Order History section keeps track of all your past orders in one list.
- You’ll see details like the order number, the date you placed it, and the total amount.
- If you Want to check something specific? Click on the order number, and it’ll take you to a full summary page with all the details about that order.

### Products

![all products](/docs/readme_images/features%20/products.png)

![sort](/docs/readme_images/features%20/sort_by.png)

### Product Detail

![Product Detail](/docs/readme_images/features%20/product_detail.png)


### Product Management
**Add Product**

![add product](/docs/readme_images/features%20/add_product.png)

**Edit Product**

![edit product](/docs/readme_images/features%20/edit_product.png)

**Delete Product**

![delete product](/docs/readme_images/features%20/delete_product.png)


### Gromming Services

![Groominging Services](/docs/readme_images/features%20/grooming_services.png)

### Services Management
**Add Service**

![Add Service](/docs/readme_images/features%20/add_service.png)


**Edit Service**

![edit Service]

**Delete Service**

![Delete Service]


### Bag

![shopping bag](/docs/readme_images/features%20/shopping_bag.png)

### Checkout 

![checkout](/docs/readme_images/features%20/checkout.png)

**Details**

**Order Summary**

**Payment**

**Confirmation**

![order_confirmation](/docs/readme_images/features%20/confirmation.png)

### Testimonials

![Testimonials](/docs/readme_images/features%20/testimonials.png)

**Add Testimonial**

![Add Testimonial](/docs/readme_images/features%20/add_testimonial.png)

**Edit Testimonial**

![Edit Testimonial](/docs/readme_images/features%20/edit_testimonial.png)

**Delete Testimonial**

![Delete Testimonial](/docs/readme_images/features%20/delete_testimonial.png)

### Error Pages

![403 error](/docs/readme_images/features%20/403_error.png)

- 400 Bad Request - Pet Vibe is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - Due to an internal error we are unable to process this request.


## Languages

- Python
- HTML5
- CSS3
- Javascript

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
    }
```

- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Push these changes to Github.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                              |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                              |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.


## AWS Set Up
### AWS S3 Bucket
- Create an AWS account.
- From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
- Click 'Create a new bucket', give it a name(match your Heroku app name if possible), and choose the region closest to you.
- Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred.
- Uncheck block all public access and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.


### IAM
- From the 'Services' menu, search IAM and select it.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions' as per above.
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Give your user a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables as per above list and also in your env.py.


### Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add storages to your installed apps.
- Create an if statement in settings.py 

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell django where our static files will be coming from in production.


- Create a file called custom storages and import both our settings from django.con as well as the s3boto3 storage class from django storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/

```

- and then add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
- Your static files and media files should be automatically linked from django to your S3 bucket.

## Forking this repository
- Locate the repository at this link [Pet Vibe](https://github.com/thiago-23/Pet-Vibe).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [Pet Vibe](https://github.com/thiago-23/Pet-Vibe). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Credits

## Acknowledgments
