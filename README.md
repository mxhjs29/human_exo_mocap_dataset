# Human–Exoskeleton Motion Capture and Interaction Dataset

## 人体–外骨骼运动捕捉与交互数据集

---

## Abstract | 摘要

This repository releases a public, research-oriented dataset for studying human–exoskeleton motion, interaction dynamics, and task semantics. The dataset integrates human body kinematics represented by the SMPL model, exoskeleton motion states, human–exoskeleton interaction forces, task-level semantic annotations, and estimated interaction stiffness between the human and the exoskeleton. It is intended to support research in human–robot interaction, exoskeleton control, biomechanics, imitation learning, and embodied intelligence.

本仓库公开发布一个面向科研的人体–外骨骼运动与交互数据集。数据集系统性地整合了基于 SMPL 的人体运动学数据、外骨骼运动状态、人机交互力、任务级语义信息，以及人体–外骨骼之间的交互刚度估计结果。该数据集可用于人机交互、外骨骼控制、生物力学、模仿学习与具身智能等研究方向。

### Human-Exoskeleton Model
* <img src="https://github.com/user-attachments/assets/e68a8cc3-e290-4949-9736-5266fa45d233"
     alt="正视图-穿戴外骨骼"
     width="600" />

* <img src="https://github.com/user-attachments/assets/a07b1eb2-75d4-4a73-a43d-ffdfec148c7d"
     alt="侧视图-穿戴外骨骼"
     width="600" />



---

## Dataset Overview | 数据集概览

The dataset is organized in a structured numerical format (NumPy-compatible), where each data sample corresponds to a synchronized human–exoskeleton interaction instanc
Each data entry includes **13 core fields**, covering kinematics, dynamics, interaction, reward-related quantities, and semantic annotations.

数据以结构化数值形式（兼容 NumPy）存储，每个样本对应一次同步的人体–外骨骼交互记录，包含 **13 个核心字段**，覆盖运动学、动力学、人机交互、奖励相关量以及任务语义信息。

---

## Data Fields Description | 数据字段说明

### 1. Human Motion (SMPL) | 人体运动（SMPL）

* `smpl_pos`
  SMPL pose parameters representing the full-body human motion.
  基于 SMPL 模型的人体全身姿态参数。

* `human_data`
  Auxiliary human-related features (e.g., kinematic or physiological descriptors).
  人体相关的辅助特征量（如运动学或生理特征描述）。

---

### 2. Exoskeleton Motion | 外骨骼运动数据

* `qpos_exo_right`, `qpos_exo_left`
  Joint positions of the right and left exoskeleton subsystems.
  右/左外骨骼系统的关节位置。

* `qvel_exo_right`, `qvel_exo_left`
  Joint velocities of the right and left exoskeleton subsystems.
  右/左外骨骼系统的关节速度。

---

### 3. Human–Exoskeleton Interaction | 人机交互量

* `f_interactive_right`, `f_interactive_left`
  Measured or estimated interaction forces between the human and the exoskeleton on the right and left sides.
  人体与外骨骼在右/左侧的交互力（测量或估计）。

* `K_fitness_right`, `K_fitness_left`
  Estimated interaction stiffness (or compliance-related coefficients) between the human and the exoskeleton.
  人体–外骨骼之间的交互刚度（或顺应性相关系数）。

---

### 4. Task Semantics | 任务语义

* `text`
  High-level task or gesture semantic description (natural language).
  任务或手势的高层语义描述（自然语言）。

---

### 5. Reward and Task-Related Signals | 奖励与任务相关信号

* `rwd_action`
  Action-related reward signal.
  与动作执行相关的奖励信号。

* `rwd_pos`
  Position-related reward signal.
  与位置或姿态相关的奖励信号。

---

## Video Demonstrations | 视频演示

### Gesture Demonstrations | 手势示例

* **Gesture Video 1**: 

https://github.com/user-attachments/assets/f1ff457d-4c0b-4e05-b6f0-55aaea672fff

* **Gesture Video 2**: 

https://github.com/user-attachments/assets/3985a5b1-2a2c-4cae-a668-27aa75285012

### Tai Chi Demonstration | 太极动作示例

* **Tai Chi Video**: 

https://github.com/user-attachments/assets/13261c06-9dbb-4b3e-8314-7c33c518f91f

### Lifting and Carrying Tasks | 搬运动作示例

* **Lifting Video 1**:
  
https://github.com/user-attachments/assets/951ef130-630d-4cad-8552-0add4cf0ff0c

* **Lifting Video 2**:

https://github.com/user-attachments/assets/19b8f8f3-b0dc-478f-ae65-b6d98c9d9b3c

---

## License

This dataset is released for **academic research purposes only**. Please refer to the LICENSE file for detailed terms.

本数据集仅供**学术研究使用**，具体使用条款请参见 LICENSE 文件。

---

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{human_exo_mocap_dataset,
  title     = {Human--Exoskeleton Motion Capture and Interaction Dataset},
  author    = {Muyuan, Ma and Shuo Chen and collaborator},
  year      = {2026},
  url       = {https://github.com/mxhjs29/human_exo_mocap_dataset}
}
```
```bibtex
@article{zhang2025motionxpp,
  title     = {Motion-X++: A Large-Scale Multimodal 3D Whole-Body Human Motion Dataset},
  author    = {Zhang, Y. and Lin, J. and Zeng, A. and Wu, G. and Lu, S. and Fu, Y. and others and Zhang, L.},
  journal   = {arXiv preprint arXiv:2501.05098},
  year      = {2025},
}
```
```bibtex
@article{averta2021ulimb,
  title   = {U-Limb: A Multi-Modal, Multi-Center Database on Arm Motion Control in Healthy and Post-Stroke Conditions},
  author  = {Averta, G. and Barontini, F. and Catrambone, V. and Haddadin, S. and Handjaras, G. and Held, J. P.},
  journal = {GigaScience},
  volume  = {10},
  number  = {6},
  pages   = {giab043},
  year    = {2021},
}
```
```bibtex
@misc{cmu_mocap,
  title        = {CMU Graphics Lab Motion Capture Database},
  author       = {{Carnegie Mellon University}},
  howpublished = {\url{http://mocap.cs.cmu.edu/}},
  note         = {Online; accessed as a motion capture dataset},
}
```
```bibtex
@article{caggiano2022myosuite,
  title   = {MyoSuite: A Contact-Rich Simulation Suite for Musculoskeletal Motor Control},
  author  = {Caggiano, V. and Wang, H. and Durandau, G. and Sartori, M. and Kumar, V.},
  journal = {arXiv preprint arXiv:2205.13600},
  year    = {2022},
}
```
```bibtex
@incollection{loper2023smpl,
  title     = {SMPL: A Skinned Multi-Person Linear Model},
  author    = {Loper, M. and Mahmood, N. and Romero, J. and Pons-Moll, G. and Black, M. J.},
  booktitle = {Seminal Graphics Papers: Pushing the Boundaries, Volume 2},
  pages     = {851--866},
  year      = {2023},
  publisher = {Springer},
}
```

---

## Contact

For questions or collaboration, please open an issue or contact the repository maintainer.

如有问题或合作意向，请通过 Issue 或联系仓库维护者。
