import multiprocessing

def process1(conn):
    conn.send("Hello from Process 1")
    msg = conn.recv()
    print("Process 1 received:", msg)
    conn.close()

def process2(conn):
    msg = conn.recv()
    print("Process 2 received:", msg)
    conn.send("Hello back from Process 2")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=process1, args=(parent_conn,))
    p2 = multiprocessing.Process(target=process2, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()