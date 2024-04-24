# python-lambda-api

## Install the following
- Python 3.9
- npm (https://github.com/nvm-sh/nvm), but default exports path to .bash_profile. If there is no .zshrc file (check by using command ```open -e ~/.zshrc```), then create one using ```touch ~/.zshrc```, then run installation script.
- After restarting terminal, might have to run command ```source ~/.zshrc```
- Install node & npm using command: ```nvm install node```
- Install npm serverless: ```npm install -g serverless``` (https://www.npmjs.com/package/serverless)
- Install AWS CLI: [steps](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
- Serverless Offline ```npm install serverless-offline --save-dev```
- serverless plugin ``serverless plugin install -n serverless-python-requirements"``

## Deploying and testing code
- Configure AWS CLI: ```aws configure```
- To run API locally: ```sls offline```. Do cntrl + c in order to suspend.
- To deploy to dev: ```serverless deploy```

## Debugging/Common issues
- If sls offline is already running on port, err msg: ```{ Error: listen EADDRINUSE: address already in use ::1:3002```. Then list the processes in that port: ```lsof -i tcp:<port number```, then kill the node process running: ```kill -9 <PID>```.
- 