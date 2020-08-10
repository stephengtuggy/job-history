# job-history

[![stephengtuggy](https://circleci.com/gh/stephengtuggy/job-history.svg?style=shield)](https://circleci.com/gh/stephengtuggy/job-history)

## Overview

This is a web app that lets you enter info about your current and past jobs into a database. You can then view this info later on, when you need to fill out a job application. This way, you won't have to remember everything every time. And you can refine the wording on, for example, your "Contributions and Accomplishments" section over time.

## Prerequisites

This app runs in `Docker`. You will need both Docker and Docker Compose to build and run it. On macOS and Windows, the easiest way to get these products is to download and install Docker Desktop Community Edition.

Also, you will need a copy of a file called `.env`. Ask me for this file, and I can send you one, via a more secure channel than GitHub. Place this file in the root folder of your local working copy of this repo.

Once you have these items in place, run the command `docker-compose up --build`, either in PowerShell on Windows, or in Terminal on macOS or Linux. You should see Docker Compose pulling the latest copy of each source docker image, then building the main image for this app, and finally, spinning up both containers.

Assuming that this command completes successfully, you can now open your favorite web browser, and enter the URL: [http://localhost:8000/administrate/](http://localhost:8000/administrate/). Oh, wait. The first time you run this app, you will need to create a user account for yourself. To do so, open another PowerShell / Terminal window in the `app` folder, and run this sequence of commands, one at a time:

```sh
docker-compose exec web bash
./manage.py createsuperuser
exit
```

After the createsuperuser command, follow the prompts to set up your first user account / login. You should then be able to log in at [the above URL](http://localhost:8000/administrate/). From that point, you can create other user accounts if you wish using the web UI.

## Use

Now, down to business. Under `JOB HISTORY`, click on `EMPLOYERS`, and enter your employers, one at a time. (Employers that you have worked for in the past ten years is probably sufficient.)

Finally, click on the `JOB HISTORY` breadcrumb; click on `POSITIONS`; and start entering the positions you have held at each employer, along with the time periods for each.

Good luck!

P.S. Feel free to submit issues or Pull Requests for any additional fields that should be added for data that is required on any job application. This app is intended to be as all-inclusive as possible when it comes to data fields.

Thanks!
