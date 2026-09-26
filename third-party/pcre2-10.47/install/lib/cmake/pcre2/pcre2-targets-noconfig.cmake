#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "pcre2::pcre2-8-static" for configuration ""
set_property(TARGET pcre2::pcre2-8-static APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pcre2::pcre2-8-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "C"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libpcre2-8.a"
  )

list(APPEND _cmake_import_check_targets pcre2::pcre2-8-static )
list(APPEND _cmake_import_check_files_for_pcre2::pcre2-8-static "${_IMPORT_PREFIX}/lib/libpcre2-8.a" )

# Import target "pcre2::pcre2-posix-static" for configuration ""
set_property(TARGET pcre2::pcre2-posix-static APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pcre2::pcre2-posix-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "C"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libpcre2-posix.a"
  )

list(APPEND _cmake_import_check_targets pcre2::pcre2-posix-static )
list(APPEND _cmake_import_check_files_for_pcre2::pcre2-posix-static "${_IMPORT_PREFIX}/lib/libpcre2-posix.a" )

# Import target "pcre2::pcre2-8-shared" for configuration ""
set_property(TARGET pcre2::pcre2-8-shared APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pcre2::pcre2-8-shared PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libpcre2-8.so.0.15.0"
  IMPORTED_SONAME_NOCONFIG "libpcre2-8.so.0"
  )

list(APPEND _cmake_import_check_targets pcre2::pcre2-8-shared )
list(APPEND _cmake_import_check_files_for_pcre2::pcre2-8-shared "${_IMPORT_PREFIX}/lib/libpcre2-8.so.0.15.0" )

# Import target "pcre2::pcre2-posix-shared" for configuration ""
set_property(TARGET pcre2::pcre2-posix-shared APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pcre2::pcre2-posix-shared PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libpcre2-posix.so.3.0.7"
  IMPORTED_SONAME_NOCONFIG "libpcre2-posix.so.3"
  )

list(APPEND _cmake_import_check_targets pcre2::pcre2-posix-shared )
list(APPEND _cmake_import_check_files_for_pcre2::pcre2-posix-shared "${_IMPORT_PREFIX}/lib/libpcre2-posix.so.3.0.7" )

# Import target "pcre2::pcre2grep" for configuration ""
set_property(TARGET pcre2::pcre2grep APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pcre2::pcre2grep PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/bin/pcre2grep"
  )

list(APPEND _cmake_import_check_targets pcre2::pcre2grep )
list(APPEND _cmake_import_check_files_for_pcre2::pcre2grep "${_IMPORT_PREFIX}/bin/pcre2grep" )

# Import target "pcre2::pcre2test" for configuration ""
set_property(TARGET pcre2::pcre2test APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pcre2::pcre2test PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/bin/pcre2test"
  )

list(APPEND _cmake_import_check_targets pcre2::pcre2test )
list(APPEND _cmake_import_check_files_for_pcre2::pcre2test "${_IMPORT_PREFIX}/bin/pcre2test" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
