strace
======

system call tracing
===================

syscall
=======

========= == ======
userspace -> kernel
========= == ======

syscall
=======

========= == ======
userspace -> kernel
========= == ======
your app  ->  kernel
========= == ======

syscall
=======

========= == ======
userspace -> kernel
========= == ======
your app  ->  kernel
CPU       vs  I/O
========= == ======


demo: shell
===========

demo: screw1
============

demo: screw2
============

syscalls
========

> 300


syscalls: read
==============

read readv recv recvmsg recvfrom


syscalls: write
===============

write writev send sendto sendmsg


syscalls: files
===============

open opendir/readdir stat link symlink


syscalls: files
===============

openat opendirat statat linkat symlinkat


syscalls: processes
===================

clone execve exit_group

non-syscalls: processes
=======================

time.time() / gettimeofday


demo: async
===========

demo: nginx
===========
