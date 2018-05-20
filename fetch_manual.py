# import urllib
#
# urllib.urlretrieve('http://us1.php.net/get/php_manual_en.tar.gz/from/this/mirror')

import os
import tarfile
import urllib.request

file_name = 'php_manual_en.tar.gz'

if not os.path.isfile(file_name):
    manual_url = "http://us1.php.net/get/php_manual_en.tar.gz/from/this/mirror"
    remote_file = urllib.request.urlopen(manual_url)
    meta = remote_file.info()
    file_size = int(meta.__getitem__('Content-Length'))
    print("Downloading: %s Bytes: %s" % (file_name, file_size))
    archive_file = open('./%s' % file_name, 'wb')
    archive_file.write(remote_file.read())
    archive_file.close()

manual_archive = tarfile.open('./%s' % file_name)
print("Extracting %s" % file_name)
tarfile.TarFile.extractall(manual_archive)
print("Docs extracted to ./php-chunked-xhtml")

print("Removing %s" % file_name)
os.remove('./%s' % file_name)
