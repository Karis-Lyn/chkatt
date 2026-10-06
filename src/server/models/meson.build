libs = files(
  'dbctrl.c',
  'user.c'
)

c_lib_dir = meson.current_source_dir() / '..' / 'c_lib'
inc = include_directories('../../public')
message('wrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrry: ', c_lib_dir)

mysql_dep = dependency('mariadb', required: true)
openssl_dep = dependency('openssl', required: true)
pcre2_dep = declare_dependency(
  link_args: ['-L' + c_lib_dir, '-lpcre2-8'],
  include_directories: inc
)
foreach src : libs
  full_path = src.full_path()
  file_name = full_path.split('/')[-1]
  no_suffix = file_name.replace('.c', '')
  shared_library(
    no_suffix,
    file_name,
    install: true,
    install_dir: 'c_lib',
    dependencies: [mysql_dep, openssl_dep, 
    pcre2_dep],
    include_directories: inc
  )
endforeach
