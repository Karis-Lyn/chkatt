libs = files(
  'dbctrl.c',
  'user.c'
)
mysql_dep = dependency('mariadb', 'mysqlclient', required: true)
inc = include_directories('../../public')
foreach src : libs
  full_path = src.full_path()
  file_name = full_path.split('/')[-1]
  no_suffix = file_name.replace('.c', '')
  shared_library(
    no_suffix,
    file_name,
    install: true,
    install_dir: 'c_lib',
    dependencies: mysql_dep,
    include_directories: inc
  )
endforeach
