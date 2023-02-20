from subprocess import call

cmd = "display notification \" 有新微博！！ \" with title \"lironghao_weibo_robot\""
call(["osascript", "-e", cmd])