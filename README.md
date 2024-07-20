# job-history

[![stephengtuggy](https://circleci.com/gh/stephengtuggy/job-history.svg?style=shield)](https://circleci.com/gh/stephengtuggy/job-history)

## Overview

This is a web app that lets you enter information about your current and past jobs into a database. You can then refer to this information later on, when you need to fill out a job application. This way, you won't have to remember everything every time. And over time, you can refine the wording on, for example, your "Contributions and Accomplishments" section.

## Prerequisites

This app runs in `Docker`. You will need Docker to build and run it. The process for installing Docker varies between platforms. You should use a recent-enough version of Docker that it comes bundled with Docker Compose.

Also, you will need a copy of a file called `.env`. Place this file in the root folder of your local working copy of this repository. You can use `.env.example` as a template. Be sure to set the value for `JOB_HISTORY_SECRET_KEY`, ideally to a high-quality password generated by a password generator.

Once you have these items in place, run the command `docker compose up --build`, either in PowerShell on Windows, or in Terminal on macOS or Linux. You should see Docker Compose pulling the latest copy of the source Docker image, then building this application's Docker image based on that, and finally, spinning up the container.

Assuming that this command completes successfully, you can now open your favorite web browser, and enter the URL: [http://localhost:8000/administrate/](http://localhost:8000/administrate/). Oh, wait. The first time you run this app, you will need to create a user account for yourself. To do so, open another PowerShell / Terminal window in the `app` folder, and run this sequence of commands, one at a time:

```sh
docker compose exec web sh
./manage.py createsuperuser
exit
```

After the createsuperuser command, follow the prompts to set up your first user account. You should then be able to log in at [the above URL](http://localhost:8000/administrate/). From that point, you can create other user accounts if you wish using the web UI.

## Use

Now, down to business. Under `JOB HISTORY`, click on `EMPLOYERS`, and enter your employers, one at a time. (Entering the employers that you have worked for in the past ten years is probably sufficient.)

Finally, click on the `JOB HISTORY` breadcrumb; click on `POSITIONS`; and start entering the positions you have held at each employer, along with the time periods for each.

Good luck!

P.S. Feel free to submit issues or Pull Requests for any additional fields that should be added for data that is required on any job application. This app is intended to be as all-inclusive as possible when it comes to data fields.

Thanks!
