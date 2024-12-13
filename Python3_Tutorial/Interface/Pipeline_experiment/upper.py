import sys; 
import multiprocessing as mproc; 

def upper_task_01(conn): 
    conn.send("mul \\\"Nerc\\\", 2"); 
    msg = conn.recv(); 
    print("Upper Case: " + msg.upper()); 
    conn.close(); 

if __name__ == '__main__':
    upper_conn, cli_conn = mproc.Pipe()

    import CLI; 
    CLI.cli_out = cli_conn; 
    
    upper_proc = mproc.Process(target=upper_task_01, args=(upper_conn,)); 
    cli_proc = mproc.Process(target=CLI.cli_task, args=(cli_conn,)); 

    upper_proc.start(); cli_proc.start(); 
    upper_proc.join(); cli_proc.join(); 