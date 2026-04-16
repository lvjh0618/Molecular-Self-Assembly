import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_xvg(filename, title="MD Simulation Analysis", ylabel="Values"):
    """
    读取 GROMACS .xvg 文件并绘制学术图表
    """
    # 自动跳过 XVG 文件的注释行 (@ 和 #)
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith(('@', '#')):
                data.append([float(x) for x in line.split()])
    
    df = pd.DataFrame(data, columns=['Time (ps)', 'Value'])

    # 设置学术风格
    plt.figure(figsize=(8, 5), dpi=300)
    plt.plot(df['Time (ps)']/1000, df['Value'], color='#1f77b4', linewidth=1.5, label='BBR System')
    
    # 图表修饰
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Time (ns)', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # 自动保存
    output_name = filename.replace('.xvg', '.png')
    plt.savefig(output_name)
    print(f"✅ 图表已保存为: {output_name}")
    plt.show()

# 使用示例 (测试时可以先注释掉)
# plot_xvg('rmsd.xvg', title="Root Mean Square Deviation", ylabel="RMSD (nm)")
