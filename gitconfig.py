#coding:utf-8
import os
user_config = {
    "email":'2285020853@qq.com', 
    "name":'tuopan',
    # "template":'.git_template.txt'
}

cmd = [
"git config --global alias.co checkout",
"git config --global alias.ci commit",
"git config --global alias.st status",
"git config --global alias.br branch",
"git config --global core.editor  vim"
]

def gitCmd():
    for c in cmd:
        os.system(c)
        
def gitTemplate():
    proj_git = os.path.abspath('.')
    template_name = os.path.join(proj_git, user_config['template'])
    # print template_name
    os.system("git config --global commit.template {}".format(template_name))

def userConfig():
    os.system("git config --global user.email '{}' ".format(user_config['email']))
    os.system("git config --global user.name '{}' ".format(user_config['name']))

def gitConfigCheck():
    os.system('git config --list')
    pass

def main():
    gitCmd()
    userConfig()
    # gitTemplate()
    gitConfigCheck()

if __name__ == '__main__':
    print('*'*10)
    main()
    print('*'*10)

