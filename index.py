linknguon = 'https://www.taipm.net/abcccc/cdeeee/index.html'
linklink = '../../images/test.png'
def checkurl(linknguon, linklink):
  if linknguon[(len(linknguon)-1):len(linknguon)] == '/':
    linknguon = linknguon[0:(len(linknguon)-1)]
  if linklink[0:8] == 'https://' or linklink[0:7] == 'http://':
    return linklink
  else:
    withouthttp = linknguon[linknguon.rindex('//')+2:len(linknguon)]
    cutt = withouthttp.split('/')
    giaothuc = ''
    if linknguon[0:8] == 'https://': giaothuc = 'https://'
    if linknguon[0:7] == 'http://': giaothuc = 'http://'
    if linklink[0:2] == '//':
      return giaothuc + linklink[2:len(linklink)]
    else:
      if linklink.count("../") != -1:
        return giaothuc + "/".join(cutt[0:len(cutt)-1-linklink.count("../")]) + '/' + linklink.replace("../", "")
      else:
        if linklink[0:1] == '/':
          return giaothuc + cutt[0] + linklink
        if linklink[0:1] != '/':
          return giaothuc + "/".join(cutt[0:len(cutt)-1]) + '/' + linklink
print(checkurl(linknguon, linklink))
