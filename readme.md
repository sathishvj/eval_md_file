Todo before you run the python script:
    - change value of gcp\_enablement\_content\_folder. It should point to where you have cloned the git repository.

If you're testing code, make updates to the file sample\_data/madeup/en.md. Then check if it works by running the python code. (Your python executable might be different):
    - python3 main.py sample\_data/madeup

To run it on actual en.md file, provide the full path to the lab folder. The lab folder should have an en.md file in it.

This seems to be a properly written lab to check with: /Users/vj/coding/projects/gcp-enablement-content/labs/tc013-l200-net-accl22-former-cloud-ids/instructions
    - python3 main.py /Users/vj/coding/projects/gcp-enablement-content/labs/tc013-l200-net-accl22-former-cloud-ids/instructions
