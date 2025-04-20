import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output_field.delete(1.0, tk.END)  

    if result.returncode == 0:
        output_field.insert(tk.END, result.stdout)
    else:
        output_field.insert(tk.END, result.stderr )

# GUI 
root = tk.Tk()
root.title("HDFS GUI")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)


output_field = tk.Text(root, wrap=tk.WORD, font=("Courier", 14))
output_field.pack(fill='both', expand=True, padx=10, pady=5)

# tab Cluster & Control 
frame_cluster = ttk.Frame(notebook)
notebook.add(frame_cluster, text="Cluster Control")

def run_cluster_cmd(cmd):
    run_command(cmd)
def start_dfs():
    run_cluster_cmd("start-dfs.sh")

def start_yarn():
    run_cluster_cmd("start-yarn.sh")

def stop_dfs():
    run_cluster_cmd("stop-dfs.sh")

def stop_yarn():
    run_cluster_cmd("stop-yarn.sh")

def check_jps():
    run_cluster_cmd("jps")

ttk.Button(frame_cluster, text="Start DFS", command=start_dfs, width=20).pack(pady=5)
ttk.Button(frame_cluster, text="Start YARN", command=start_yarn, width=20).pack(pady=5)
ttk.Button(frame_cluster, text="Stop DFS", command=stop_dfs, width=20).pack(pady=5)
ttk.Button(frame_cluster, text="Stop YARN", command=stop_yarn, width=20).pack(pady=5)
ttk.Button(frame_cluster, text="Check JPS", command=check_jps, width=20).pack(pady=5)

# tab List & Cat 
frame_list_cat = ttk.Frame(notebook)
notebook.add(frame_list_cat, text="List & Cat")

path_entry = ttk.Entry(frame_list_cat, font=("Courier", 12))
path_entry.pack(padx=10, pady=10, fill='x')

def list_hdfs():
    run_command(f"hdfs dfs -ls {path_entry.get()}")

def cat_hdfs():
    run_command(f"hdfs dfs -cat {path_entry.get()}")

def get_hdfs():
    run_command(f"hdfs dfs -get {path_entry.get()}")

ttk.Button(frame_list_cat, text="List", command=list_hdfs, width=20).pack(pady=5)
ttk.Button(frame_list_cat, text="Cat", command=cat_hdfs, width=20).pack(pady=5)
ttk.Button(frame_list_cat, text="Get", command=get_hdfs, width=20).pack(pady=5)

# tab Copy &  Move 
frame_copy_move = ttk.Frame(notebook)
notebook.add(frame_copy_move, text="Copy & Move")

ttk.Label(frame_copy_move, text="Source Path:").pack()
src_entry = ttk.Entry(frame_copy_move, font=("Courier", 12))
src_entry.pack(padx=10, pady=5, fill='x')

ttk.Label(frame_copy_move, text="Destination Path:").pack()
dst_entry = ttk.Entry(frame_copy_move, font=("Courier", 12))
dst_entry.pack(padx=10, pady=5, fill='x')

def copy_hdfs():
    run_command(f"hdfs dfs -cp {src_entry.get()} {dst_entry.get()}")

def move_hdfs():
    run_command(f"hdfs dfs -mv {src_entry.get()} {dst_entry.get()}")

ttk.Button(frame_copy_move, text="Copy", command=copy_hdfs, width=20).pack(pady=5)
ttk.Button(frame_copy_move, text="Move", command=move_hdfs, width=20).pack(pady=5)

# tab Append & Put 
frame_append_put = ttk.Frame(notebook)
notebook.add(frame_append_put, text="Append & Put")

local_frame = ttk.Frame(frame_append_put)
local_frame.pack(pady=5, fill='x')

ttk.Label(local_frame, text="Local File:").pack(side=tk.LEFT, padx=5)
local_entry = ttk.Entry(local_frame, font=("Courier", 12))
local_entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

def browse_local_file():
    file_path = filedialog.askopenfilename()
    local_entry.delete(0, tk.END)
    local_entry.insert(0, file_path)

ttk.Button(local_frame, text="Browse", command=browse_local_file).pack(side=tk.LEFT)

# Entry for HDFS destination
ttk.Label(frame_append_put, text="HDFS Path:").pack()
hdfs_entry = ttk.Entry(frame_append_put, font=("Courier", 12))
hdfs_entry.pack(padx=10, pady=5, fill='x')

def append_hdfs():
    run_command(f"hdfs dfs -appendToFile {local_entry.get()} {hdfs_entry.get()}")

def put_hdfs():
    run_command(f"hdfs dfs -put {local_entry.get()} {hdfs_entry.get()}")

ttk.Button(frame_append_put, text="Append", command=append_hdfs, width=20).pack(pady=5)
ttk.Button(frame_append_put, text="Put", command=put_hdfs, width=20).pack(pady=5)

# tab Remove & Make Dir 
frame_remove_mkdir = ttk.Frame(notebook)
notebook.add(frame_remove_mkdir, text="Remove & Mkdir")

ttk.Label(frame_remove_mkdir, text="HDFS Path:").pack()
rm_mkdir_entry = ttk.Entry(frame_remove_mkdir, font=("Courier", 12))
rm_mkdir_entry.pack(padx=10, pady=5, fill='x')

def remove_hdfs():
    run_command(f"hdfs dfs -rm -r {rm_mkdir_entry.get()}")

def mkdir_hdfs():
    run_command(f"hdfs dfs -mkdir {rm_mkdir_entry.get()}")

ttk.Button(frame_remove_mkdir, text="Remove", command=remove_hdfs, width=20).pack(pady=5)
ttk.Button(frame_remove_mkdir, text="Make Directory", command=mkdir_hdfs, width=20).pack(pady=5)



# Start GUI
root.mainloop()

