import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime
import logging
import Logger

import Crawlers, IO_Helper, Upload

if __name__ == '__main__':
    # relativePath = str(pathlib.Path().resolve())
    # print(relativePath)
    # local = False
    # page_end = 21  # check for top 500 people
    # if relativePath.startswith('C:'):
    #     local = True
    
    # submission_record_file = 'submission_record.json'
    # submission_record = IO_Helper.loadSubmissionRecord(submission_record_file, {})
    
    Contest_Metadata = IO_Helper.loadContestMetaData()
    rootLogger = Logger.getRootLogger()

    for contest_title_slug in Contest_Metadata:

        startTime = Contest_Metadata[contest_title_slug]['startTime']
        
        currTime = time.time()

        if startTime > currTime: continue   # case where next contest info is in meta data

        print('Processing now [Contest=%s]' % contest_title_slug)

        # contest = IO_Helper.loadFile('contest', '65').strip()
    
        # contest_int = (int)(contest)

        # Crawlers.fetch_rank_and_crawl_submission(contest_title_slug)
        # break

        IO_Helper.parse_and_runJPLag(contest_title_slug)
        # break

        # Upload.uploadFolder(contest_title_slug, [])
        Upload.upload(rootLogger)

        # IO_Helper.commit_and_pushtoGithub('compare_record_.json')

        # contest_int = contest_int + 1

        # IO_Helper.writeFile('contest', str(contest_int))
        # IO_Helper.writeRecord(submission_record, submission_record_file)
    # IO_Helper.countAllSubmissions()
        break