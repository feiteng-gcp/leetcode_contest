import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime
import logging

import Crawlers, IO_Helper, uploadToGCP

if __name__ == '__main__':
    # relativePath = str(pathlib.Path().resolve())
    # print(relativePath)
    # local = False
    # page_end = 21  # check for top 500 people
    # if relativePath.startswith('C:'):
    #     local = True
    
    # submission_record_file = 'submission_record.json'
    # submission_record = IO_Helper.loadSubmissionRecord(submission_record_file, {})
    while True:
        
        contest = IO_Helper.loadFile('contest', '65').strip()
    
        contest_int = (int)(contest)

        Crawlers.fetch_rank_and_crawl_submission(contest_int)

        IO_Helper.parse_and_runJPLag(contest_int)

        uploadToGCP.uploadFolder('JPLAGResult/' + contest)

        IO_Helper.commit_and_pushtoGithub('compare_record.json')

        contest_int = contest_int + 1
        IO_Helper.writeFile('contest', str(contest_int))
        # IO_Helper.writeRecord(submission_record, submission_record_file)
    # IO_Helper.countAllSubmissions()