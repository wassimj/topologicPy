if(NOT "/root/wasim-cpython-topologic/Topologic/cmake-3.15.2/Tests/CMakeTests" MATCHES "^/")
  set(slash /)
endif()
set(url "file://${slash}/root/wasim-cpython-topologic/Topologic/cmake-3.15.2/Tests/CMakeTests/FileDownloadInput.png")
set(dir "/root/wasim-cpython-topologic/Topologic/cmake-3.15.2/Tests/CMakeTests/downloads")

file(DOWNLOAD
  ${url}
  ${dir}/file3.png
  TIMEOUT 2
  STATUS status
  EXPECTED_HASH SHA1=5555555555555555555555555555555555555555
  )
