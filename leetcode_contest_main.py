import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime

import Crawlers, IO_Helper, uploadToGCP

if __name__ == '__main__':

    debug = False
    page_end = 20   # check for top 500 people
    while True:
        # try:
        contest = IO_Helper.loadContest().strip()
        contest_int = (int)(contest)


        print(contest)
        
        # if not debug: 
        Crawlers.fetchContestRankingPage(contest)
        # if not debug: 
        Crawlers.crawlSubmissions(contest, page_end)
        
        if not debug: IO_Helper.jplag(contest)

        # if not debug: update_indexMD()
        IO_Helper.writeToHTML()
        


        # if not debug: commit_and_pushtoGithub('JPLAGResult/' + contest)
        # if not debug: 
        uploadToGCP.uploadFolder('JPLAGResult/' + contest)
        if debug: 
            print('finished..')
            break

        if not debug: IO_Helper.commit_and_pushtoGithub('index.html')

        if not debug: contest_int = contest_int + 1


        IO_Helper.writeContest(contest_int)
        # except Exception as err:
        #     print(err)
        #     pass
            

        # if page_end < 500: break   


