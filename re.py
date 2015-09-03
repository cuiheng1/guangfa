#------------------------------------------------------------------------------
def testPrevPostMatch():
    # post match:       (?=xxx)
    # post non-match:   (?!xxx)
    # prev match:       (?<=xxx)
    # prev non-match:   (?<!xxx)

    #note that input string is:
    #src=\"http://b101.photo.store.qq.com/psb?/V10ppwxs00XiXU/5dbOIlYaLYVPWOz*1nHYeSFq09Z5rys72RIJszCsWV8!/b/YYUOOzy3HQAAYqsTPjz7HQAA\"
    qqPicUrlStr             = 'src=\\"http://b101.photo.store.qq.com/psb?/V10ppwxs00XiXU/5dbOIlYaLYVPWOz*1nHYeSFq09Z5rys72RIJszCsWV8!/b/YYUOOzy3HQAAYqsTPjz7HQAA\\"';
    qqPicUrlInvalidPrevStr  = '1234567http://b101.photo.store.qq.com/psb?/V10ppwxs00XiXU/5dbOIlYaLYVPWOz*1nHYeSFq09Z5rys72RIJszCsWV8!/b/YYUOOzy3HQAAYqsTPjz7HQAA\\"';
    qqPicUrlInvalidPostStr  = 'src=\\"http://b101.photo.store.qq.com/psb?/V10ppwxs00XiXU/5dbOIlYaLYVPWOz*1nHYeSFq09Z5rys72RIJszCsWV8!/b/YYUOOzy3HQAAYqsTPjz7HQAA123';
    canFindPrevPostP = r'(?<=src=\\")(?P<qqPicUrl>http://.+?\.qq\.com.+?)(?=\\")';
    qqPicUrl = "";

    foundPrevPost = re.search(canFindPrevPostP, qqPicUrlStr);
    print "foundPrevPost=",foundPrevPost; #
    if(foundPrevPost):
        qqPicUrl = foundPrevPost.group("qqPicUrl");
        print "qqPicUrl=",qqPicUrl; # qqPicUrl= http://b101.photo.store.qq.com/psb?/V10ppwxs00XiXU/5dbOIlYaLYVPWOz*1nHYeSFq09Z5rys72RIJszCsWV8!/b/YYUOOzy3HQAAYqsTPjz7HQAA
        print "can found qqPicUrl here";

    foundInvalidPrev = re.search(canFindPrevPostP, qqPicUrlInvalidPrevStr);
    print "foundInvalidPrev=",foundInvalidPrev; # foundInvalidPrev= None
    if(not foundInvalidPrev):
        print "can NOT found qqPicUrl here";

    foundInvalidPost = re.search(canFindPrevPostP, qqPicUrlInvalidPostStr);
    print "foundInvalidPost=",foundInvalidPost; # foundInvalidPost= None
    if(not foundInvalidPost):
        print "can NOT found qqPicUrl here";

    return ;