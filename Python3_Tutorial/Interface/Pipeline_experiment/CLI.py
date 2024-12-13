#命令行程序

#如果希望同一个程序既能在CLI和Tkinter GUI下均能执行(基于multiprocessing.Pipe), 
#不建议在CLI下直接使用Print, 因为Print的默认参数可能会导致管道传递的结果出现混乱

#与命令行有关的库
from cmd import Cmd; 
import sys; 
import multiprocessing as mproc; 
from pdb import set_trace as Breakpoint; 

#用于实现累积加法和乘法命令的库
import operator as oper; 
from functools import reduce; 
    
#输出端初始化
cli_out = sys.stdout; 

#重定向输出(也可在模块外直接使用"="语句)
def cli_output_redirect(target):
    global cli_out; 
    cli_out = target; 
    
#根据输出流的对接口自定义输出模式
def cli_output(text): 
    global cli_out;
    #通过命令行调用, 直接使用Print(需要附带适当的参数)打印到控制台(conhost/bash)
    if cli_out == sys.stdout or cli_out == sys.stderr: 
        print(text, file=cli_out, flush=True);
    #通过multiprocessing.Pipe调用, 使用Pipe链接对象的send方法, 将数据传送驱动模块
    elif type(cli_out) == mproc.connection.PipeConnection: 
        cli_out.send(text); 
    #通过其他方式调用的输出方法, 尚处于构思阶段
    else: 
        pass; 
    
class CLI(Cmd): 
    
    #直接调用命令行程序
    if __name__ == "__main__":
        prompt = "Sample CLI>"; 
    
    #提示符被用户提交空行时, 不作任何处理(默认为执行上一条命令)
    def emptyline(self): 
        pass; 

    #退出会话
    def do_quit(self, arg):
        print("Exiting CLI session...", 
            file=sys.stderr, flush=True); 
        cli_output(""); 
        return True; 
    
    def help_quit(self): 
        print("Quit CLI session. \nUsage: quit\n", 
            file=sys.stderr, flush=True); 
        cli_output(""); 
        
    #累积加法命令(只是一个示例)
    def do_add(self, arg): 
        sum = reduce(oper.add, eval(arg)); 
        cli_output(str(sum)); 
        
    def help_add(self): 
        print("Get sum of elements in a sequence. \n" + 
            "Usage: add e1, [e2, ...]\n", end="",
            file=sys.stderr, flush=True);
        cli_output(""); 
        
    #累积乘法命令(只是一个示例)
    def do_mul(self, arg): 
        prod = reduce(oper.mul, eval(arg)); 
        cli_output(str(prod)); 
        
    def help_mul(self): 
        print("Get product of elements in a sequence. \n" + 
            "Usage: mul e1, [e2, ...]\n", end="",
            file=sys.stderr, flush=True);
        cli_output(""); 

#直接调用命令行程序, 才会启动CLI会话, 否则, 由管道传输数据
if __name__ == "__main__":
    CLI().cmdloop(); 
else: 
    def do_(command, arg):
        task = f'CLI.do_{command}(CLI, \"{arg}\")'; 
        return exec(task); 
    
    def cli_task(conn): 
        global cli_out; 
        #从驱动模块接收并处理命令语句
        msg = conn.recv(); 
        idx_arg_sep = msg.index("\x20"); 
        command = msg[0: idx_arg_sep]; arg = msg[idx_arg_sep + 1: ]; 
        #执行语句并输出结果
        cli_out = conn; 
        status = do_(command, arg); 
        