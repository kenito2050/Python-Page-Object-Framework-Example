url = 'https://svcrel.wn.nasinsurance.com/index.php?c=app_list.list'
# Create a list of each bit between slashes
slashparts = url.split('/')
# Now join back the first three sections 'http:', '' and 'example.com'
basename = '/'.join(slashparts[:3]) + '/'
# All except the last one
dirname = '/'.join(slashparts[:-1]) + '/'
print ('slashparts = %s' % slashparts)
print ('basename = %s' % basename)
print ('dirname = %s' % dirname)