# how-to :: Use FileZilla
---
## Overview
FileZilla is a program that allows a user to exchange files between a server and a client.

### WARNING
FileZilla's installer contains malware program that you want to avoid installing.

### Estimated Time Cost: 0.2 hrs

### Why FileZilla? Why not GitHub or WinSCP?
First of all, WinSCP is designed for Windows and has more features than FileZilla. If you're on Windows, you should probably just use WinSCP. We chose FileZilla because we know that not everyone’s personal device operates on Windows.
 
While GitHub provides a means of transferring files, that isn’t its main focus. FileZilla will not have an upper file size limit, and also not have a middleman service that stores the files for you. If your goal is to simply move data from a server to your personal computer or vice versa, FileZilla does that job easily. 

### Prerequisites:

- Know your StuyCS username and password for the StuyCS lab computers
- FileZilla works for Windows, Mac, and Linux
- Have FileZilla installed
- You can install FileZilla [here](https://filezilla-project.org/download.php)

1. Open FileZilla
2. Fill in the Host, Username, and Password fields on top.
   For “Host”, you can use the IP addresses of the computers in any of the 4 StuyCS labs. Add ```sftp://``` before all of the IP addresses.
   ```
   sftp://149.89.161.1xx
   sftp://149.89.160.1xx
   sftp://149.89.151.1xx
   sftp://149.89.150.1xx

   ```
   Replace “xx” with any computer number in that lab. Example: 149.89.161.133 for computer #33 in room 351.
   Leave Port empty.
3. Quickconnect and trust the host.
4. You are finished. You can try dragging a text file or directory from the Stuy server to your computer.
5. FileZilla wiki [here](https://wiki.filezilla-project.org/Using#Quick_Guide)


### Resources
* https://wiki.filezilla-project.org/Using#Quick_Guide

---

Accurate as of (last update): 2022-10-26

#### Contributors:  
  Ryan Lee, pd 8
  Joseph Jeon, pd 8
  Samson Wu, pd 8
