# Thoughtexchange Feedback Report Implementation

## Project Resources:
1. [Knowledge Document](https://docs.google.com/document/d/1SFzbvQMX8EYySmgS58m-XInGEQ4IR6XABX2-q02-Hm4/edit?usp=sharing): Learn more about the Harvard students initially involved in this project, our goals, the background for the work we’ve done so far, our proposed solution, our design process, and our current product.

2. [Website](https://bibbfeedback.herokuapp.com/report_generator/): Check out our website here! School admin are able to upload a file (exchangedata.csv) with data containing thoughts from teachers on a prompt asked through ThoughtExchange, select thoughts they find relevant and interesting, provide summary and action items, and email their findings and thoughts in a feedback report to send to teachers, admin, etc. [Sample CSV File](https://drive.google.com/file/d/1qoBUbLoTdW1KwHjLW20icQj49r_Derir/view?usp=sharing) to use to upload to the website

3. [Figma](https://www.figma.com/file/yAKEcs3l5xDnKJKU8SaHwn/CS96-TE-Upload?node-id=0%3A1): Figma is a vector graphics editor and prototyping tool which is primarily web-based and was used to prototype our design before it was implemented. Feel free to play around with the current design so you can see what it looks like before implementing it using code!

## Relevant Files:

### Report Generator Python Files
`report_generator/views.py` - A view is a “type” of Web page in the Django application that generally serves a specific function and has a specific template. In Django, web pages and other content are delivered by views. Each view is represented by a Python function. Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name). This app has six views: `index(request)`, `upload_file(request)`, `preview(request)`, `instructions(request)`, `handler404(request)`, and `handler500(request)`. 

`report_generator/urls.py` - Django uses `URLconf` (URL configuration), which is a set of patterns that Django will try to match the requested URL to find the correct view. The list of URL patterns makes sure that each link corresponds to the correct view. 

`report_generator/utils.py` - This file contains the functions we need to handle the data and contains the functions `handle_uploaded_file(f)`, `handle_results(form)`, and `send_email(results_data)`. 

`report_generator/forms.py` - Django has a built-in `Form` class that allows us to add different forms to our website quickly. We created `UploadFileForm(forms.Form)`, `ResultsForm(forms.Form)`, and `EmailForm(forms.Form)` classes to upload a file, select certain thoughts and write paragraphs with a summary and action items, and accept someone's email. 

### Report Generator Template HTML Files

`report_generator/template/upload.html` - HTML page for uploading a file to the site

`report_generator/template/instructions.html` - HTML page that contains instructions for how to download a CSV file from Thoughtexchange and upload it to our application

`report_generator/template/review.html` - HTML page that shows the uploaded Thoughtexchange data and forms to check off relevant responses, complete a summary, add action items, and enter an email to send the final report to

`report_generator/template/success.html` - HTML page that shows the generated email sent to the email address provided

`report_generator/template/email.html` - HTML email template sent to the email address provided

## How to run this project on your own local computer using the Terminal

1. Clone this repository in the desired directory

        git clone git@github.com:aurielws/bibb-deployment.git

* or 
        
        git clone https://github.com/Aurielws/bibb-deployment

2. Install virtualenvwrapper (if not already installed)

* Linux, Mac:
        
        sudo pip3 install virtualenv

* Windows:
        
        pip3 install virtualenv

3. Move inside the project

        cd bibb-deployment
        
4. Create virtual environment

        virtualenv venv -p python3

5. Activate virtual environment

* Linux, Mac:

        source venv/bin/activate
        
* Windows:

        .\venv\Scripts\activate

6. Install required packages

        pip3 install -r requirements.txt

7. Run project

        python3 manage.py migrate
        python3 manage.py runserver

8. Deactivate virtual environment when done

        deactivate

