Change the BlackArch/Archlinux Default GRUB's background.

About

    I've been using Blackarch for some time. Every time I look at the grub screen that starts by default, it's very monotonous.
    So I wrote this script to change grub's default background, just for fun!

How to use ?
    First saved your favorite PNG image  and the script file in the same directory.
    and then ..

root@ArchLinux:~ # uname -a                                       
Linux ArchLinux 4.11.9-1-ARCH #1 SMP PREEMPT Wed Jul 5 18:43:47 CEST 2017 i686
root@ArchLinux:~ # 
root@ArchLinux:~ # file blackarch.png                            
blackarch.png: PNG image data, 1920 x 1080, 8-bit/color RGBA, non-interlaced
root@ArchLinux:~ # 
root@ArchLinux:~ # python change_grub_background.py blackarch.png 

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|                           Notice:                                         |
|   This python script is test SUCCESSFULLY on Archlinux distrubtion        |
|            for changed the GRUB's default background                      |
|   It will modifield the config file "/etc/defalut/grub"                   |
|        You can choice one favorite IMAGE.PNG replace defalut              |
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 
[*]The image file is [ blackarch.png ] ...
[+]Configuration file is done ...
[*]Coping image file done ...
Generating grub configuration file ...
Found theme: /usr/share/grub/themes/starfield/theme.txt
Found linux image: /boot/vmlinuz-linux
Found initrd image(s) in /boot: initramfs-linux.img
Found fallback initrd image(s) in /boot: initramfs-linux-fallback.img
done
[*]All done. Restarting and look at the effect ..

## Restarting the system you will see the result..##
