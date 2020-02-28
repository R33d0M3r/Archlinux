#!/usr/bin/python

import shutil,os,sys

banner = '''\033[2;34m
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|                           Notice:                                         |
|   This python script is test SUCCESSFULLY on Archlinux distrubtion        |
|            for changed the GRUB's default background                      |
|   It will modifield the config file "/etc/defalut/grub"                   |
|        You can choice one favorite IMAGE.PNG replace defalut              |
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
\033[0m '''

def change_grub_image(image_name):
    try:
        grub_config_path = '/etc/default/grub'
        contents = 'GRUB_THEME="/usr/share/grub/themes/starfield/theme.txt"'

        # get image file
        image_name = sys.argv[1]

        if not os.path.exists(image_name):
            print('[!]Image file not found ...')
            sys.exit(-3)
        print('[*]The image file is [ %s ] ...' % (image_name))

        try:
            # config defalut grub file .
            with open (grub_config_path,'a+') as f:
                f.write(contents + str('\n'))
            print('[+]Configuration file is done ...')
        except:
            pass

        dist_pah = '/usr/share/grub/themes/starfield/starfield.png'
        shutil.copyfile(image_name, dist_pah)
        print('[*]Coping image file done ...')

    except PermissionError as e:
        print(e)

if __name__ == '__main__':
    print(banner)
    if len(sys.argv) < 2:
        print('\033[2;31m[*]\033[0mUsage:sudo python %s IMAGE_FILE ' % sys.argv[0])
        sys.exit(-1)

    if os.getuid() != 0:
        print('\033[2;31m[*]The script must be run as root ...\033[0m')
        sys.exit(-2)

    change_grub_image(sys.argv[1])

    ret = os.system('grub-mkconfig -o /boot/grub/grub.cfg')
    if ret == 0:
        print('[*]All done. Restarting and look at the effect ...')
    else:
        print('[!]Oooh,Something has error, try later ...')

