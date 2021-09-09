import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime

import uploadToGCP

contest = 183
for i in range(contest, 65, -1):
    uploadToGCP.uploadFile('JPLAGResult/contest')
