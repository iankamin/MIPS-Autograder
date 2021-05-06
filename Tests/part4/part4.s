grader/                                                                                             0000755 0001750 0001750 00000000000 14044372454 011613  5                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 grader/__pycache__/                                                                                 0000755 0001750 0001750 00000000000 14044372440 014016  5                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 grader/__pycache__/__init__.cpython-38.pyc                                                          0000644 0001750 0001750 00000000456 14044060151 020203  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 U
    e`�`�   �                   @   s<   d dl m Z  d dlmZ d dlmZmZmZ d dlmZ dS )�   )�
autograder)�concat)�settings�Test�Show)�	runGraderN)r   r   r   r   r   �wrapperr   � r	   r	   �//home/kamian/MIPS_Autograder/grader/__init__.py�<module>   s                                                                                                                                                                                                                     grader/__pycache__/autograder.cpython-38.pyc                                                        0000644 0001750 0001750 00000025637 14044372440 020620  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 U
    ��`7;  �                   @   sd  d dl Z d dlZd dlZd dlZd dlZzd dlmZmZmZ W n    d dlmZmZmZ Y nX ej	�
e�d Zd3d
d�Zdd� Zdd� Zd4dd�Zdd� Zdd� Zdd� Zdd� Zdd� ad5ed�dd�Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)d*� Zd6d,d-�Zd7d.d/�Zed0k�r`e� ej	�
ej!d  �� zej!d1 Z"W n   ej#Z"Y nX ee"d2� dS )8�    N)�settings�Test�Show�/FT�
output.txt�graderResults.txt�settings.json�concat.sc           &         sx  | d krt |�an| atj}|at|d�at��  |r�t|�}	t� \}
}}t	tj�d t	|
�krddnd}z|
d �
� }W n   d}Y nX t|||	|||� ntddddd|� g }
t	tj�}dd� t|�D �}dd� t|�D �}d	d� t|�D �}g � t|�D �]�}tj| }|j}t|
|�\}}t	|j�d
k�rb|j}� fdd�|D � � jt	d� � ��  ng }|j||< tjd
k�r�t|d |||� nt|d ||d � tjd
k�r� D ]}|�|d�}�q�d|k�r�t�d� n&d|k�r�nt	|�
� �dk�rd||< t	|�}t|�D ]�\}}z|| }W n   d}Y nX ||k�rb||  |j| 7  < d||< n6||k�r||  d|j | 7  < |�|�}d||< �q|| }|j�r�|| |jk �r�t�d� d
}t�d|| |jf � t�d� |||< �q d}i } d
}!tjd
k�rTt|�}"|"tjk�r,tj}!ntjt|� tj }!t�d|!tjf � tjd
k�rd|!}#tjdk�s|tjdk�r�d
}#tjd
k�r�|!| d< tjd
k�s�tjdk�r�|#t|d tj� �7 }#|#| d< t	|tjd � �d
k�r�t|tjd � �}$|$| d< tjdk�r2td|d �D ]}||d  | d| < �qd| i}%t�d� t�t�|%�� t��  |�rtt ttj!��"� � d S )N�w�   z2Program Terminated Early without running all tests� �����c                 S   s   g | ]}d �qS �r   � ��.0�_r   r   �1/home/kamian/MIPS_Autograder/grader/autograder.py�
<listcomp>%   s     zautograder.<locals>.<listcomp>c                 S   s   g | ]}d �qS r   r   r   r   r   r   r   &   s     c                 S   s   g | ]}d �qS r   r   r   r   r   r   r   '   s     r   c                    s   g | ]}� � |��qS r   )�append)r   �f�ZprevUserInputr   r   r   2   s     )�key�   z<NON ASCII DATA>zH
Non-Ascii characters were found in your prompt credit cannot be given 
�<NO PROMPT FOUND>Zgarbage_sdakfjlkasdjlfkg      �?z?
Extra Credit must work fully to receive credit
original score z - %.3f out of %s
z-............................................
TzPrompt - %.3f out of %s
�   �PromptZTotalzExtra Creditztest%i�scoresz

======== RESULTS ========
)#r   �io�AllTests�
outputFile�open�autograderResultsZprintHeader�mips�GetMipsOutput�len�strip�PrintMipsError�range�ExpectedAnswers� getStudentPromptAndOutputPerTest�	UserInput�sort�reverse�ExtraCredit�PromptGrade�ShowDetails�replace�write�	enumerate�OutOf�index�sumZNumberOfRegularTests�	JsonStyle�json�dumps�close�print�name�read)&ZIO�_ShowAll�runMips�printResultsZ
outputDestZautograderOutput�settingsFile�
concatFile�tests�	SPIMerror�output�header_error�NoneAsciiMSG�completionErr�
lastOutputZTotalNumTestsZpromptPointsZ
testPointsZ	EC_Points�testNum�testZexpectedAns�StudentOutput�StudentPromptr+   �lineZnumOfrequiredAns�iZea�indZtempZsimpleGrader   r   �pp�totalZectotalZ
JSONscoresr   r   r   �
autograder   s�     

  




  

   






 
 rS   c                 C   s�   z| |d  � � }W n   d}Y nX z| |d d  }W n   d}Y nX |�dd�}d|krn|�dd�}qXdd	� |�d�D �}||fS )
Nr   r   r   �<NO OUTPUT FOUND>�
z
   �

c                 S   s   g | ]}|� � �qS r   �r&   )r   �rr   r   r   r   �   s     z4getStudentPromptAndOutputPerTest.<locals>.<listcomp>)r&   r1   �split)rE   rJ   rM   rL   r   r   r   r*   �   s      
  
 r*   c                  C   sh   t js
dS tt �� �} t| �dkrd| �d� ttd d�}|�d�	| �� |�d� |�
�  dt S dS )Nr   r   z"YOU SHOULD NOT BE ABLE TO SEE THISz	input.txtr
   rU   z < %sinput.txt )r   �RequiresUserInput�listZgetAllUserInputLinesr%   r   r!   �localDir�
writelines�joinr:   )�linesZ	inputFiler   r   r   �generateInput�   s     

r`   c                 C   s�   t jdt dd� t jdt dd� t� }tjr6d}nd}td }| dkrTtd }n| }d	j||||td
�}zt j|ddd� W n$ t jk
r�   Y dS    Y dS X dS )Nzecho "" > %sT)�shellzecho "" > %serror.txtz-bare r   �	error.txtr	   zBspim {baremode} -file {concat} {userinput} >> {output} 2>> {error})Zbaremode�concat�errorZ	userinputrE   r   )ra   �timeoutz:    Your Program Timed Out due to an infinite loop in MIPSz:    UH-OH your program failed to run for an unknown reason)	�
subprocess�callr    r\   r`   r   �BareMode�format�TimeoutExpired)rB   Z	userInputrh   Z	errorpathZ
concatpath�instructionr   r   r   r#   �   s0      
  �r#   c                  C   sN  d} z$t tdd��}|�� }W 5 Q R X W n�   t tdd��}|�� }W 5 Q R X tdd� t�tdd�|�D ��}|D ]F\}}tt�	|||� d	��}|d |� td
| d� ||d �  }qtd} |�
dd�}t td dd��}|�|� W 5 Q R X Y nX |�d�}dd� |D �}|�d�}|�dd�}t|�dk�r@|d �� nd}||| fS )Nr   rX   )�mode�rbc                 S   s    g | ]}|� d �|�d �f�qS r   )�start�end)r   �mr   r   r   r   �   s     z!GetMipsOutput.<locals>.<listcomp>z[^ -]+zutf-8�bigz<NON ASCII DATA>( %s )z!non ascii characters were printedr1   zoutput2.txtr
   z
XXFFVV3793
c                 S   s   g | ]}|� � �qS r   rW   )r   �or   r   r   r   �   s     r   rU   �   )r!   r    r=   �reversed�re�finditer�bytes�hex�int�
from_bytes�decoder\   r2   rY   �popr%   r&   )rG   r   rE   ZprobIndices�s�eZascrF   r   r   r   r$   �   s*       ( 

r$   c           
   	   C   s�  t �d� t �d� d}ttd d��}|�� �� }W 5 Q R X t|�dkrV||d 7 }t|�dkrn||d 7 }t|�dkr�||d 7 }t|�dkr�||d 7 }t| �dkr�|| �� d 7 }|r�ttd d��}|�� �� }	W 5 Q R X nd	}	t|	�dk�r|d
|	 7 }d|	k�r|d7 }nt|	�dk�r.|d7 }t|�dk�rL||�� d 7 }t|�dk�rjt �|�� � n
t �d� t �d� d S )Nz
the following errors occurred
z=============================
r   zconcatErrors.txtrX   r   rV   rb   z7program was never run due to potential illegal syscallszruntime error:
   %s
z"Attempt to execute non-instructionz:   ^^^ Your subroutine must terminate with a JUMP RETURN

rU   z	    None
z=============================

)r"   r2   r!   r\   r=   r&   r%   )
Z	headerErrrI   rD   ZNonAsciiMSGrH   r?   Z	allErrorsr   Z	concatErrZMIPSerrr   r   r   r'   �   s>    

 

  
r'   c                 C   s$   t | � t| � t| � td� d S )NrU   )�PrintMemInputs�PrintRegInputs�printUserInputr;   �rK   r   r   r   �	ShowInput  s    r�   c                 C   s   t |� t| |d� d S �NT)�PrintStudentPrompt�printOutput�rK   rL   rM   r   r   r   �
ShowOutput  s    r�   c                 C   s0   t | � t| � t|� t| � t| |d� d S r�   )r   r�   r�   r�   r�   r�   r   r   r   �ShowAll  s
    r�   r�   c                 C   s�   t �d|  � |jrt �d� |j}tj}|jtjkr:d S tjtjkrVt �d|  � n
t �d� |jtjkr~t �d� t	|� |jtj
kr�t �d� t|||� |jtjkr�t|||� t �d|  � d S )NzTEST %i z(Extra Credit) z=========== test%i ==========
z
Sample Output
==============
z(Input Only)
z(Output Only)
zTEST %i)r"   r2   r.   �	ShowLevelr   r   �NONE�ALLZINPUTr�   ZOUTPUTr�   r�   )rJ   rK   rL   rM   �T�Ir   r   r   r0     s&     
  


r0   c                 C   sB   t | j�dkrt�d� | jD ]}t�d|j|j|jf � qd S )Nr   z
Initial Data in Memory -->
z   addr(%s) =  %s "%s")r%   �	MemInputsr"   r2   �addr�type�data)rK   �inpr   r   r   r   0  s     

r   c                 C   sB   t | j�rt�d� | jD ]"}t|j�}t�d|j|f � qd S )Nz
Register Input Values -->
z   reg: %s = %s
)r%   �	RegInputsr"   r2   �GetHexAndDecOrString�value�reg)rK   r�   �valr   r   r   r�   5  s
    
 


r�   c                 C   s@   | d kr<t �d� t| �� �dk r.t �d� nt �d|  � d S )Nz
Your Prompt -->
r   z   <NO PROMPT WAS FOUND>
�   %s
)r"   r2   r%   r&   )rM   r   r   r   r�   ;  s
    
r�   c                 C   s8   | j }t|�dkrt�d� |D ]}t�d| � q d S )Nr   z
User Input -->
r�   )r+   r%   r"   r2   )rK   �flrN   r   r   r   r�   C  s
     
r�   c                 C   s�  |rt �d� t| j�D �]�\}}|jd kr�t| j| t|j��}t �d|j	|f � z,t|| t|j��}t �d|j	|f � W q   z$||  t �d� t �|| � W n4   d|kr�t �d|j	|f � n
t �|� Y nX Y qX qqt �d| j| |jf � z6|| }t
|�� �dk�r(d}t �d	||jf � W q   z$||  t �d
� t �|| � W n6   d|k�r�t �d	||jf � n
t �|� Y nX Y qX qqd S )Nz
Output -->
z Expected   %s = %s
z   Actual   %s = %s

z0   <FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT>
rT   z Expected   %s at address %s
r   zNO STRING WAS FOUNDz   Actual   %s at address %s

z.   FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT
)r"   r2   r3   �Outputr�   r�   r)   ry   r�   r�   r%   r&   )rK   rL   Z_printHeaderrO   ZEoutputZExAnsZ
studentAnsrX   r   r   r   r�   I  sF    




r�   c                 C   s"   zt | � W dS    Y dS X d S )NTF)ry   )r}   r   r   r   �Is_intr  s
     r�   �    c                 C   s    t | �} t| d|>  d|>  �S )Nr   )ry   rx   )r�   Znbitsr   r   r   �to_hexx  s    r�   c                 C   sv   | � � } |dkr0t| �dkr0dtt| ��| f S t| �rHd| t| �f S | dd� dkrrdt| dd � d	�| f S | S )
N�   r   z %s ( '%s' )z	%s ( %s )r   �0xz	%s ( %i )r   �   )r&   r%   r�   �ordr�   ry   )r}   r�   r   r   r   r�   |  s       r�   �__main__r   )r>   )NFTTr   r   r   r	   )r	   )N)r�   )r   )$r8   �os�sysrf   ru   Zgrader.settingsr   r   r   �path�dirname�__file__r\   rS   r*   r`   r#   r$   r'   r�   r�   r�   r0   r   r�   r�   r�   r�   r�   r�   r�   �__name__�chdir�argvr>   r�   r   r   r   r   �<module>   sN            �
w
.)


                                                                                                   grader/__pycache__/wrapper.cpython-38.pyc                                                           0000644 0001750 0001750 00000001730 14044051456 020130  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 U
    #S�`�  �                   @   s�   d dl mZ d dlZd dlZz(d dlmZ d dlmZ d dlmZ W n    d dlmZmZmZ Y nX ddd�Ze	dkr�e�
ej�ejd  �� e�  dS )�    )�runN)�settings)�
autograder)�concat)r   r   r   �settings.json�submission.s�
output.txt�concat.s�graderResults.txtFTc           
   	   C   sX   zt jd }W n   d}Y nX |p&|}t| �}t|||d�}	t|||	||||d� d S )N�   F)�IO�sfile�
concatFile)r   �_ShowAll�runMips�
outputDestr   �autograderOutput�printResults)�sys�argvr   r   r   )
�settingsFile�submissionFile�
outputFiler   r   �ShowAllr   r   �ior   � r   �./home/kamian/MIPS_Autograder/grader/wrapper.py�	runGrader   s      
 �r   �__main__)r   r   r   r	   r
   FT)�
subprocessr   r   �osr   r   r   �graderr   �__name__�chdir�path�dirnamer   r   r   r   r   �<module>   s"            �
                                        grader/__pycache__/settings.cpython-38.pyc                                                          0000644 0001750 0001750 00000021055 14044072557 020317  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 U
    nu�`c#  �                   @   s�   d dl Z d dlZd dlZd dlZd dlmZ G dd� de�ZG dd� d�ZG dd� d�Zd	d
� Z	e
dkr�e�ej�ejd  �� ed�Ze�� Ze jedd�Zee� dS )�    N)�Enumc                   @   s<   e Zd ZdZdZdZdZdd� Zdd� Zd	d
� Z	dd� Z
dS )�Showr   �   �   �   c                 C   s   | j |j kS �N��value��self�other� r   �//home/kamian/MIPS_Autograder/grader/settings.py�__gt__
   �    zShow.__gt__c                 C   s   | j |j kS r   r   r
   r   r   r   �__ge__   r   zShow.__ge__c                 C   s   | j |j k S r   r   r
   r   r   r   �__lt__   r   zShow.__lt__c                 C   s   | j |j kS r   r   r
   r   r   r   �__le__   r   zShow.__le__N)�__name__�
__module__�__qualname__�NONE�INPUT�OUTPUT�ALLr   r   r   r   r   r   r   r   r      s   r   c                   @   s@   e Zd Zddd�Zdd� Zddd�Zd	d
� Zdd� Zdd� ZdS )�settingsNc              	   K   sV  |d kr| j f |� d S t|d��}t�|�}W 5 Q R X || _|d | _t|�dd��| _t|�dd��| _	t|�d| j	��| _
t|�dd��| _|�d	d
�| _|�dd�| _|�dd�| _|�dd�| _|�dd�| _t| j�tkr�| j�� dk| _t| j�tk�r| j�� dk| _t| j�tk�r6| j�� dk| _d| _| j|d |dd�| _d S )N�r�subroutine_name�PromptGrader   �	TestGrader   �ECTestGrade�	ShowLevel�MessageToStudent� �BareModeF�Shuffle�	JsonStyle�RequiresUserInput�true�testsT)�
canShuffle)�empty�open�json�load�io�SubroutineName�float�getr   r   r    r   r!   r"   r$   r%   r&   r'   �type�str�lower�NumberOfRegularTests�CreateTests�AllTests)r   �file�kwargs�fr/   r   r   r   �__init__   s0     
   zsettings.__init__c                 K   sB   d | _ d | _d | _d | _d | _d | _tj| _d| _	d| _
g | _d S )NF)r/   r0   r   r   r    r"   r   r   r!   r$   r'   r8   �r   r:   r   r   r   r+   2   s    zsettings.emptyFc           	      C   sv   g g  }}t |�D ]2\}}t| ||d�}|jr:|�|� q|�|� q| jrd|rdt�|� t�|� t|�| _|| S )N)�parent�testjs�
testNumber)	�	enumerate�Test�ExtraCredit�appendr%   �random�shuffle�lenr6   )	r   Zalltests_jsonr/   r*   �regZec�ir?   �testr   r   r   r7   >   s    
 



zsettings.CreateTestsc                 c   s"   | j D ]}|jD ]
}|V  qqd S r   )r8   �	UserInput)r   rJ   �liner   r   r   �getAllUserInputLinesJ   s    

zsettings.getAllUserInputLinesc                 C   s&   t d| j � | jr"t d| j � d S )Nz

REQUIRED ROUTINE: %szGENERAL MESSAGE: %s
)�printr0   r"   �r   r   r   r   �printHeaderO   s    zsettings.printHeaderc                 C   s�   i }| j |d< | j|d< | j|d< | j|d< | j|d< | j|d< | j|d< | jj|d< | j	|d	< | j
|d
< dd� | jD �|d< |S )Nr   r   r   r    r"   r$   r'   r!   r%   r&   c                 S   s   g | ]}|� � �qS r   ��ToDict)�.0�tr   r   r   �
<listcomp>_   s     z#settings.ToDict.<locals>.<listcomp>r)   )r0   r   r   r    r"   r$   r'   r!   r	   r%   r&   r8   )r   r/   r   r   r   rR   S   s    








zsettings.ToDict)N)F)	r   r   r   r<   r+   r7   rM   rP   rR   r   r   r   r   r      s   

r   c                   @   sj   e Zd ZU eed< ddd�Zdd� Zdd	� Zd
d� Zdd� Z	G dd� d�Z
G dd� d�ZG dd� d�ZdS )rB   r>   Nr   c                 K   s�   || _ |d kr| jf |� d S tt|�dd��|j�| _|�dd��� | _|| _|�dd�| _	|�dd�pz| j	rv|j
n|j| _|�dg �| _t| j	�tkr�| j	�� d	k| _	| �|�d
g ��\| _| _| �|d �\| _| _d}d S )Nr!   r   �namerB   rC   F�OutOfrK   r(   �inputs�outputs)r>   r+   �maxr   r2   r!   �strip�testNamer@   rC   r    r   rW   rK   r3   r4   r5   �	setInputs�	MemInputs�	RegInputs�
setOutputs�ExpectedAnswers�Output)r   r>   r?   r@   r:   rI   r   r   r   r<   e   s      zTest.__init__c                 K   s6   d| _ d| _tj| _d| _g | _g | _g | _g | _	d S )NrB   Fr   )
r\   rC   r   r   r!   rW   rK   r^   r_   rb   r=   r   r   r   r+   x   s    z
Test.emptyc                 C   s�   i }| j |d< | j|d< | j| jr*| jjn| jjkr>d|d< n
| j|d< | j| jjkr^tjj	n| jj	|d< | j
|d< dd� | jD �|d	< |d	  d
d� | jD �7  < dd� | jD �|d< |S )NrV   rC   r   rW   r!   rK   c                 S   s   g | ]}|� � �qS r   rQ   �rS   rI   r   r   r   rU   �   s     zTest.ToDict.<locals>.<listcomp>rX   c                 S   s   g | ]}|j s|�� �qS r   )�
memPointerrR   rc   r   r   r   rU   �   s      c                 S   s   g | ]}|� � �qS r   rQ   rc   r   r   r   rU   �   s     rY   )r\   rC   rW   r>   r    r   r!   r   r   r	   rK   r^   r_   rb   )r   r?   r   r   r   rR   �   s    



"
zTest.ToDictc                 C   s�   g }g }|D ]�}zx|� | �|d |d |d �� z0|d |d _|� | j|d |d dd�� W n" tk
r� } zW 5 d }~X Y nX W n tk
r�   Y nX z|� | �|d |d �� W q tk
r�   Y qX q||fS )	N�addr�datar3   rH   �����T)rd   r	   )rD   �__MemInput__rH   �__RegInput__�KeyError)r   rX   �	memInputs�	regInputs�inp�er   r   r   r]   �   s"     "    zTest.setInputsc                 C   s�   g }g }|D ]�}|d }|� |� z$|� | jdd|d |d�� W qW n" tk
rh } zW 5 d }~X Y nX z"|� | j|d |d |d�� W q   td	��Y qX q||fS )
N�CorrectAnswer�4�a0re   )r3   rH   re   ro   r3   rH   )r3   rH   ro   zOutput not address or register)rD   �
__Output__rj   �	Exception)r   �	outputsJSra   rY   �out�ansrn   r   r   r   r`   �   s    
 " zTest.setOutputsc                   @   s   e Zd Zddd�Zdd� ZdS )zTest.__RegInput__Fc                 C   s"   d|� dd� | _|| _|| _d S )N�$r#   )�replacerH   r	   rd   )r   rH   r	   rd   r   r   r   r<   �   s    zTest.__RegInput__.__init__c                 C   s$   | j dkr | j�dd�| jd�S d S )NFrw   r#   )rH   r	   )rd   rH   rx   r	   rO   r   r   r   rR   �   s    
zTest.__RegInput__.ToDictN)F�r   r   r   r<   rR   r   r   r   r   ri   �   s   
ri   c                   @   s   e Zd Zddd�Zdd� ZdS )zTest.__MemInput__Nc                 C   sh   || _ || _|| _|| _d|�� krd| j�dd�| _| j�dd�| _| j�dd�| _d| j d | _d S )N�asciiz\"�quote_7654123�"r#   )re   rf   r3   rH   r5   rx   )r   re   rf   r3   rH   r   r   r   r<   �   s    zTest.__MemInput__.__init__c                 C   s:   | j | j| j�dd�d�}| jd k	r6| j�dd�|d< |S )Nr|   r#   )r3   re   rf   rw   rH   )r3   re   rf   rx   rH   �r   �dr   r   r   rR   �   s    
 zTest.__MemInput__.ToDict)Nry   r   r   r   r   rh   �   s   
rh   c                   @   s   e Zd Zddd�Zdd� ZdS )zTest.__Output__Nc                 C   s�   |d kr|d krt d��|d k	r4d|�dd� | _n|| _t|�| _|| _|| _|d krld| _d| _d| _	n`|d k	r�d|�dd� | _d|�
� kr�|�
� dd � �d�}d|d d	�  | _d|d	d �  | _	d S )
Nz!reg or addr must be given a valuerw   r#   z$0�0�0xr   �   �   )rs   rx   rH   r4   r3   re   ro   �lui_reg�
upper_addr�
lower_addrr[   �zfill)r   r3   ro   rH   re   r   r   r   r<   �   s$      
 zTest.__Output__.__init__c                 C   sB   | j | jd�}| jd k	r"| j|d< | jd k	r>| j�dd�|d< |S )N)r3   ro   re   rw   r#   rH   )r3   ro   re   rH   rx   r}   r   r   r   rR   �   s    
 

 zTest.__Output__.ToDict)NNry   r   r   r   r   rr   �   s   
rr   )Nr   )r   r   r   r   �__annotations__r<   r+   rR   r]   r`   ri   rh   rr   r   r   r   r   rB   b   s   


rB   c                 C   s"   zt | � W dS    Y dS X d S )NTF)r1   )�valr   r   r   �isInt�   s
    r�   �__main__zsettings.jsonr�   )�indent)r-   �os�sysrE   �enumr   r   r   rB   r�   r   �chdir�path�dirname�argv�ttrR   r~   �dumps�jrN   r   r   r   r   �<module>   s    O                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    grader/__pycache__/concat.cpython-38.pyc                                                            0000644 0001750 0001750 00000016034 14044051456 017722  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 U
    #S�`�$  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlmZmZ W n   d dlmZmZ Y nX ej�e	�d Z
e
Zdd� Zdd� Zdd	� Zd
d� Zdd� Zdd� Zdd� Zd!dd�Zdd� Zdd� Zdd� Zdd� Zdd� Zed kr�e�ej�ejd  �� e�  dS )"�    N)�settings�Test�/c           
      C   s�  t td d��}|�d� W 5 Q R X z$t | d��}|�� }W 5 Q R X W �n   t | d��}|�� }W 5 Q R X dd� t�tdd	�|�D �}t�td
d	�tdd	�|�}|�d	�}d}|D ]f\}}|d |� �	d�d ||d � �
d�|  }}|||� d||   |||�  }	||	d 7 }q�t td d��}|�d| � W 5 Q R X Y nX |�dd�}|�dd�}|�dd�}|�dd�}|�d�}|S )N�concatErrors.txt�w�
�r�rbc                 S   s    g | ]}|� d �|�d �f�qS )r   )�start�end)�.0�m� r   �-/home/kamian/MIPS_Autograder/grader/concat.py�
<listcomp>   s     z!getSubmission.<locals>.<listcomp>z[^ -]+zutf-8z[^ -]� � �   �X�a+z�NON ASCII CHARACTER was found in your program
Attempting to fix but may cause additional issues
please check your code and remove potential problems
Potential Problems denoted with 'X' :
%s
ZXXAAXX783908782388289038339z#XXAAXX783908782388289038339 #�.globlz#.globl�.globalz#.globalZ
XXFFVV3793Z
studentGBG)�open�localDir�write�read�re�finditer�bytes�sub�decode�rfind�find�replace�split)
�sfile�f�
submission�probIndicesZproblems�s�eZ	linestartZlineendr   r   r   r   �getSubmission   s0     
.$ 
r+   c                 C   s�   d}| d � d�}t|�dkrH|d | d< |dd � D ]}|d| 7 }q6ttd d�}|d	|��  7 }| d � d	�D ].}|d	 }d
|ks�d|kr�|| }qt||7 }qt|| d fS )Nr   �   z.datar   r   z
.dataztemplate/TemplateStaticHeaderr   r   r   r   )r$   �lenr   r   r   )r'   Z
dataConcatZ	dataCheck�sectZS_Header�liner   r   r   �mergeMemory1   s    

r0   c                 C   sp   ddddddddg}g }|� d	�D ]>}|D ]4}||k}|r*t|d
�r*|�d||�� f � daq*q"|�|� d S )Nzli zla zmove zmov zblt zble zbgt zbge r   �.textz0the pseudoinstruction ' %s' was used here -> %s
F)r$   �
notComment�append�strip�runMips�
writelines)�data�text�errorsZpseudo_listZ	used_instr/   �instZvvvr   r   r   �bareModeIllegalSyntaxL   s    
r;   c                 C   s�   d| krdS d| kr"| � dd�} qt|�� dd�}d| | ksXd| | ksXd|j | kr�d	| krnt| d	�rnd
S d| kr�t| d�r�d
S dS )Nz$v0FZ0x0�0xr   z %s z,%s z0x%s ZliT�addi)r#   �hex�lowerr2   )r/   ZsyscodeZhexcoder   r   r   �illegalSyscallsZ   s      &  r@   c                 C   s�  t td d�}|�d� tjr*t| ||� d| �� kr@|�d� | �d�D ]2}|�� }tj|krJt	|tj�rJ|�dtj � qJtj|kr�|�dtj � g }|�d�D ]�}|d }|�
d	d
�}|�� }d|kr�t	|d�r�|�d� q�t|d�r�|�d� tjs�t|d��s8t|d��s8t|d��s8t|d��s8t|d�r�da|�|� q�t|�dk�rz|�d� |D ]}|�d| � �qd|��  d S )Nr   r   r   r1   z6your .text section was found somplace it shouldn't be
z4   %s cannot be used as a label in the data section
z/   Subroutine " %s " not found in test section
r   �#z #z.The only .text should be in the skeleton code
�
   zCyour program is a subroutine it must not terminate with syscall 10
�   �   �   �   �   Fr   z�You should not be requesting user input in this submission. 
you program will not run until the following lines are removed or modified
z    %s
)r   r   r6   �io�BareModer;   r?   r$   �SubroutineNamer2   r#   r@   �RequiresUserInputr5   r3   r-   �close)r7   r8   ZbareModer9   r/   ZlinelowZillegalLinesr   r   r   �illegalSyntaxe   sB    
  





 
:
rM   c                 C   s(   | � |�}| � d�}|dkr dS ||k S )NrA   �����T)r"   )r/   �substr�index�commentr   r   r   r2   �   s
    

 r2   c                 C   sF   d}t | �d��D ].\}}d|kr4|d |�d�� }||d 7 }q|S )Nr   r   rA   )�	enumerater$   rP   )r'   �out�ir/   r   r   r   �removeComments�   s    rU   �submission.s�concat.sc              
   C   sb  |dkrt td d�an
t |d�a| d kr4td�an| adat|�}t|d �|d< t|d �|d< t|d �|d< t|�\}}t�	|� t
||tj� d}tjD ]�}t td	 d
��<}|�� }	|	�dtj�}	|	�d|j�}	|	�dt|j��}	W 5 Q R X t|�at|�}
|	�dt�}	|	�d|
�}	||	7 }q�t td d
�at�	t�� �d|�� t�	|� t��  tS )NrW   r   zsettings.jsonTr   r   r,   r   ztemplate/TemplateTrialr   z<student_subroutine>z<TEST NAME>z<TEST NUMBER>z<inputs>z	<outputs>ztemplate/TemplateStaticTrailerz<TRIALS>)r   r   �outputr   rH   r5   r+   rU   r0   r   rM   rI   �AllTestsr   r#   rJ   �testName�str�
testNumber�CreateAllInputs�inputs�CreateAllOutputsZ	S_TrailerrL   )�IOr%   �
concatFiler'   ZdataSectZtextSect�allTests�testZS_Trial�body�outputsr   r   r   �concat�   s>     
 




rf   c                 C   sJ   d}| j D ]}t�t|j|j|j�� q
| jD ]}|t|j	|j
�7 }q.|S �Nr   )�	MemInputsrX   r   �createInputMem�addrr7   �type�	RegInputs�createInputReg�reg�value)rc   r^   �inpr   r   r   r]   �   s    

r]   c                 C   s    d}| j D ]}|t|�7 }q
|S rg   )�Output�createOutput)rc   re   rS   r   r   r   r_   �   s    
r_   c              
   C   sf   d|� dd� }ttd d��>}|�� }|� d| �}|� d|�}|� d|�}|W  5 Q R � S Q R X d S )N�.r   ztemplate/TemplateInitMemoryr   z<addr>�<type>z<data>)r#   r   r   r   )�_addr�_data�_typer&   �contentsr   r   r   ri   �   s    ri   c              
   C   s�   d| � dd� } d|�� kr2d|dd � �d� }ttd d��x}|�� }|� d| �}d|kr�|� d	d|dd
�  �}|� dd|d
d �  �}n|� d	d�}|� d|�}|W  5 Q R � S Q R X d S )N�$r   r<   r,   rF   ztemplate/TemplateInitRegisterr   �<reg>z<upper_val>rD   z<lower_val>�0)r#   r4   �zfillr   r   r   )Z_regZ_valr&   rx   r   r   r   rm   �   s    rm   c              
   C   sx   t td d��`}|�� }|�d| j�}|�d| j�}|�d| j�}|�d| j�}|�d| j�}|W  5 Q R � S Q R X d S )Nztemplate/TemplateOutr   z<upper_addr>z<lower_addr>rz   z	<lui_reg>rt   )	r   r   r   r#   �
upper_addr�
lower_addrrn   �lui_regrk   )rS   r&   rx   r   r   r   rr   �   s    rr   �__main__)NrV   rW   )�json�os�sysr   �grader.settingsr   r   �path�dirname�__file__r   Z
StorageDirr+   r0   r;   r@   rM   r2   rU   rf   r]   r_   ri   rm   rr   �__name__�chdir�argvr   r   r   r   �<module>   s0     !,
,	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    grader/settings.json                                                                                0000644 0001750 0001750 00000024464 14044372457 014363  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 {
    "subroutine_name": "calculator",
    "PromptGrade": 2.0,
    "TestGrade": 2.0,
    "ECTestGrade": 0.5,
    "MessageToStudent": "",
    "BareMode": false,
    "RequiresUserInput": true,
    "ShowLevel": 0,
    "Shuffle": false,
    "JsonStyle": 0,
    "tests": [
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "1234+4321"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "5555",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "00+0183"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "183",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "23+22"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "45",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "3+21"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "24",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "83-9183"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-9100",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "00-0983"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-983",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "9999-9"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "9990",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "19-9"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "10",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "1*9999"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "9999",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "1*1"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "1",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "9999*9999"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "99980001",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "1*0"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "0",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "0001*0000"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "0",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": false,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "987*234"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "230958",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-1234+-4321"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-5555",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-23+22"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-1",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "3+-21"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-18",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-83--9183"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "9100",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "1--1"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "2",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-9999-9"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-10008",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-1*-9999"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "9999",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-1*1"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-1",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "9999*-9999"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-99980001",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-987*234"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-230958",
                    "reg": "v0"
                }
            ]
        },
        {
            "name": "Test",
            "ExtraCredit": true,
            "OutOf": 0,
            "ShowLevel": 0,
            "UserInput": [
                "-0001*0001"
            ],
            "inputs": [],
            "outputs": [
                {
                    "type": 1,
                    "CorrectAnswer": "-1",
                    "reg": "v0"
                }
            ]
        }
    ]
}                                                                                                                                                                                                            grader/concat.py                                                                                    0000644 0001750 0001750 00000022377 14044051443 013437  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 import json
import os, sys
import re
try: from grader.settings import settings,Test
except: from settings import settings,Test

localDir = os.path.dirname(__file__)+"/"
StorageDir=localDir

'''
splits student submission 
submission[0] - expected data section
submission[1] - skelton code
submission[2] - .text section
'''    
def getSubmission(sfile):
    with open(localDir + "concatErrors.txt",'w') as f: f.write('\n') 
    try:
        with open(sfile,'r') as f: 
            submission=f.read()
    except:
        with open(sfile,'rb') as f: 
            submission=f.read()
        
        probIndices=[(m.start(0),m.end(0)) for m in re.finditer(bytes('[^\x00-\x7F]+','utf-8'),submission)]
        
        submission=re.sub(bytes('[^\x00-\x7F]','utf-8'),bytes(' ','utf-8'), submission)
        submission=submission.decode('utf-8')
        
        problems=''
        for (s,e) in probIndices:
            linestart,lineend=submission[:s].rfind('\n')+1,submission[e:].find('\n')+e
            sub=submission[linestart:s]+'X'*(e-s)+submission[e:lineend]
            problems+=sub+'\n'
        with open (localDir + "concatErrors.txt",'a+') as f: f.write("NON ASCII CHARACTER was found in your program\nAttempting to fix but may cause additional issues\nplease check your code and remove potential problems\nPotential Problems denoted with \'X\' :\n%s\n"%problems)
        
    submission = submission.replace("XXAAXX783908782388289038339",'#XXAAXX783908782388289038339 #')
    submission = submission.replace(".globl",'#.globl')
    submission = submission.replace(".global",'#.global')
    submission = submission.replace("XXFFVV3793","studentGBG") #just in case its coincidentally used by the student
    submission = submission.split("XXAAXX783908782388289038339")
    #print(submission)
    return submission

'''
If the student places .data at the bottom of the code this will move it to the top 
(hopefully this should preserve the location of data in memory)
'''
def mergeMemory(submission):
    dataConcat = ""#".global main\n"

    # splits expected .text section if .data is found
    
    
    dataCheck = submission[2].split(".data")
    if len(dataCheck)>1:                    # True is '.data' is present
        submission[2]=dataCheck[0]          # assumes .text section is first (should be)
        for sect in dataCheck[1:]:          # adds the term '.data' back after split
            dataConcat+='\n.data'+sect      
    
    #   Gets the static memory data

    S_Header=open(localDir + 'template/TemplateStaticHeader','r')
    dataConcat+='\n'+S_Header.read()
    
    # organizes data found in submission[0] .global is placed at the top everything else is placed at the bottom
    for line in submission[0].split('\n'):
        line=line+'\n'
        if ".global" in line or ".globl" in line:
            dataConcat= line + dataConcat
        else:
            dataConcat+= line
    
    return dataConcat,submission[2]

def bareModeIllegalSyntax(data, text, errors):
    global runMips
    pseudo_list = ['li ', 'la ', 'move ', 'mov ', 'blt ', 'ble ','bgt ','bge ' ] 

    used_inst=[]
    for line in text.split('\n'):
        for inst in pseudo_list:
            vvv = inst in line
            if vvv:
                if notComment(line, ".text"): 
                    used_inst.append("the pseudoinstruction \' %s\' was used here -> %s\n"%(inst, line.strip()))
                    runMips=False
    errors.writelines(used_inst)

def illegalSyscalls(line, syscode):
        if "$v0" not in line: return False

        while '0x0' in line: line= line.replace('0x0','0x')
        
        hexcode=hex(syscode).replace('0x','')
        if " %s "%syscode in line or ',%s '%syscode in line or '0x%s '%hexcode.lower in line:
            if "li" in line and notComment(line,"li"): return True
            if "addi" in line and notComment(line,"addi"): return True
        return False

def illegalSyntax(data, text, bareMode):
    global io
    global runMips
    errors=open(localDir + "concatErrors.txt","a+")
    errors.writelines("\n")
    if io.BareMode: bareModeIllegalSyntax(data,text, errors)
    
    if ".text" in data.lower(): errors.writelines("your .text section was found somplace it shouldn't be\n")


    for line in data.split('\n') :
        linelow=line.lower()
        if io.SubroutineName in linelow:
            if notComment(linelow, io.SubroutineName):
                errors.writelines("   %s cannot be used as a label in the data section\n"%io.SubroutineName)

    if io.SubroutineName not in text:
        errors.writelines("   Subroutine \" %s \" not found in test section\n"%io.SubroutineName)

    illegalLines=[]
    for line in text.split('\n'):
        line = line + ' '
        line = line.replace('#', ' #')
        
        linelow=line.lower()
        if ".text" in linelow:
            if notComment(linelow, ".text"): 
                errors.writelines("The only .text should be in the skeleton code\n")
                continue
        
        if illegalSyscalls(linelow, 10): errors.writelines("your program is a subroutine it must not terminate with syscall 10\n")

        if not io.RequiresUserInput:
            if illegalSyscalls(linelow, 5) or illegalSyscalls(linelow, 6) or illegalSyscalls(linelow, 7) or illegalSyscalls(linelow, 8) or illegalSyscalls(linelow, 12) : 
                runMips=False
                illegalLines.append(line)
    
    if len(illegalLines)>0:
        errors.writelines("You should not be requesting user input in this submission. \nyou program will not run until the following lines are removed or modified\n")
        for line in illegalLines:
            errors.writelines("    %s\n"%line)

    errors.close()
        
def notComment(line, substr)           :
    index=line.find(substr)
    comment=line.find('#')
    if comment == -1: return True
    return index<comment

def removeComments(submission):
    out=""
    for i,line in enumerate(submission.split("\n")):
        if "#" in line:
            line = line[:line.index("#")]
        out += line+"\n"
    return out
def concat(IO=None,sfile="submission.s",concatFile="concat.s"):
    global inputs,io
    global runMips,output,S_Header,S_Trailer
    if concatFile == "concat.s": output=open(localDir + 'concat.s','w')
    else: output=open(concatFile,'w')

    if IO == None: io =settings("settings.json")
    else : io=IO
    
    runMips=True
    
    #with open("mipsCreator.json") as j: io=json.load(j)

    submission = getSubmission(sfile)
    submission[0] = removeComments(submission[0])
    submission[1] = removeComments(submission[1])
    submission[2] = removeComments(submission[2])
    dataSect,textSect=mergeMemory(submission)
    output.write(dataSect)

    illegalSyntax(dataSect,textSect,io.BareMode)

    allTests=""
    for test in io.AllTests:
        with open(localDir + 'template/TemplateTrial','r') as S_Trial:
            body = S_Trial.read()
            body=body.replace("<student_subroutine>",io.SubroutineName)
            body=body.replace("<TEST NAME>",test.testName)
            body=body.replace("<TEST NUMBER>",str(test.testNumber))

        inputs=CreateAllInputs(test)
        outputs=CreateAllOutputs(test)

        body=body.replace("<inputs>",inputs)
        body=body.replace("<outputs>",outputs)
        allTests+=body
        #print(allTests)
        
    S_Trailer=open(localDir + 'template/TemplateStaticTrailer','r')
    output.write(S_Trailer.read().replace("<TRIALS>",allTests))
    output.write(textSect)
    output.close()
    return runMips

def CreateAllInputs(test):
    global io
    inputs=""

    for inp in test.MemInputs:
        output.write(createInputMem(inp.addr,inp.data,inp.type))
    
    for inp in test.RegInputs:
        inputs+=createInputReg(inp.reg,inp.value)

    return inputs
        
def CreateAllOutputs(test):
    outputs=""

    for out in test.Output: 
        outputs+=createOutput(out)
    return outputs

def createInputMem(_addr,_data,_type):
    _type='.'+_type.replace(".",'')
    with open(localDir + "template/TemplateInitMemory",'r') as f:
        contents=f.read()
        contents=contents.replace("<addr>",_addr)
        contents=contents.replace("<type>",_type)
        contents=contents.replace("<data>",_data)
        return contents

def createInputReg(_reg,_val):
    _reg='$'+_reg.replace('$','')
    if '0x' in _val.strip():
        _val= '0x'+_val[2:].zfill(8)
        #print(_val)
    with open(localDir + "template/TemplateInitRegister",'r') as f:
        contents=f.read()
        contents=contents.replace("<reg>",_reg)

        if '0x' in _val:
            contents=contents.replace("<upper_val>",'0x'+_val[2:6])
            contents=contents.replace("<lower_val>",'0x'+_val[6:])
        else:
            contents=contents.replace("<upper_val>",'0')
            contents=contents.replace("<lower_val>",_val)
        
        return contents

def createOutput(out):
    with open(localDir + "template/TemplateOut",'r') as f:
        contents=f.read()
        contents=contents.replace("<upper_addr>",out.upper_addr)
        contents=contents.replace("<lower_addr>",out.lower_addr)
        contents=contents.replace("<reg>",out.reg)
        contents=contents.replace("<lui_reg>",out.lui_reg)
        contents=contents.replace("<type>",out.type)
        return contents
    






if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    concat()                                                                                                                                                                                                                                                                 grader/wrapper.py                                                                                   0000644 0001750 0001750 00000001731 14044051443 013637  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 from subprocess import run
import sys,os
try:
    from settings import settings
    from autograder import autograder
    from concat import concat
except:
    from grader import settings,autograder,concat


def runGrader(settingsFile="settings.json",submissionFile="submission.s",
              outputFile="output.txt",concatFile="concat.s",autograderOutput="graderResults.txt",
              ShowAll=False,printResults=True):
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=False # overrides json "show" and shows the StudentOutputs of every test
    _ShowAll=_ShowAll or ShowAll

    io=settings(settingsFile)

    runMips=concat(IO=io,sfile=submissionFile,concatFile=concatFile)
    autograder(IO=io,_ShowAll=_ShowAll, runMips=runMips,outputDest=outputFile, concatFile=concatFile,
    autograderOutput=autograderOutput,printResults=printResults)


if __name__ == "__main__":
    
    
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    runGrader()                                       grader/autograder.py                                                                                0000644 0001750 0001750 00000035467 14044372434 014337  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 import json
import os
import sys
import subprocess
import re
try: from grader.settings import settings,Test,Show
except: from settings import settings,Test,Show

localDir = os.path.dirname(__file__)+"/"

#os.chdir(os.getcwd()+"/"+os.path.dirname(sys.argv[0])) # ensures proper initial directory
def autograder(IO = None, _ShowAll=False, runMips=True, printResults=True,
               outputDest="output.txt",autograderOutput="graderResults.txt",
               settingsFile="settings.json",concatFile="concat.s"):
    global ShowAll, io,outputFile,autograderResults
    if IO == None: io = settings(settingsFile)
    else : io=IO
    tests = io.AllTests
    outputFile=outputDest
    autograderResults=open(autograderOutput,'w')
    
    io.printHeader()

    if runMips: 
        SPIMerror = mips(concatFile)
        output, header_error, NoneAsciiMSG = GetMipsOutput()
        completionErr="Program Terminated Early without running all tests" if len(io.AllTests)*3 > len(output) else ""
    
        try: lastOutput=output[-1].strip()
        except: lastOutput=""
        PrintMipsError( header_error, lastOutput, SPIMerror, NoneAsciiMSG, completionErr, runMips)
    else:
        PrintMipsError( "", "", "", "", "", runMips)
        output = []
    
    TotalNumTests=len(io.AllTests)
    promptPoints = [0 for _ in range(TotalNumTests)]
    testPoints = [0 for _ in range(TotalNumTests)]
    EC_Points = [0 for _ in range(TotalNumTests)]

    prevUserInput=[]
    for testNum in range(TotalNumTests):
        test=io.AllTests[testNum]
        expectedAns=test.ExpectedAnswers
        
        StudentOutput,StudentPrompt= getStudentPromptAndOutputPerTest(output,testNum)

        if len(test.UserInput)>0:
            UserInput=test.UserInput
            [prevUserInput.append(f) for f in UserInput]
            prevUserInput.sort(key=len)
            prevUserInput.reverse()
        else: UserInput=[]

        # check if test it extra credit

        EC_Points[testNum] = test.ExtraCredit

        if io.PromptGrade > 0: ShowDetails(testNum+1,test,StudentOutput,StudentPrompt)
        else:                  ShowDetails(testNum+1,test,StudentOutput,None)

        # grades student prompt
        if io.PromptGrade > 0:
            for line in prevUserInput: StudentPrompt = StudentPrompt.replace(line,"")    # removes user input if they decided to print it out
            if ("<NON ASCII DATA>" in StudentPrompt): 
                autograderResults.write("\nNon-Ascii characters were found in your prompt credit cannot be given \n")
            elif ("<NO PROMPT FOUND>") in StudentPrompt:
                None
            else:
                if len(StudentPrompt.strip())>3: promptPoints[testNum]=1

        numOfrequiredAns=len(expectedAns)
        for i,line in enumerate(StudentOutput):
            try:    ea=expectedAns[i]
            except: ea="garbage_sdakfjlkasdjlfk" #if student Output is longer than actual output the current expected answer doesnt exist

            if line == ea:
                testPoints[testNum] += test.OutOf / numOfrequiredAns
                expectedAns[i]="garbage_sdakfjlkasdjlfk"    #ensures students cant get credit if they print the same answer musltiple times
            
            elif line in expectedAns:   #if they swapped the registers they get partial credit
                testPoints[testNum] += (.5*test.OutOf) / numOfrequiredAns
                ind = expectedAns.index(line)
                expectedAns[ind]="garbage_sdakfjlkasdjlfk"
        
        temp=testPoints[testNum]
        if test.ExtraCredit and ( testPoints[testNum] < test.OutOf ):
                autograderResults.write("\nExtra Credit must work fully to receive credit\noriginal score ")
                temp=0

        autograderResults.write(" - %.3f out of %s\n"%(testPoints[testNum],test.OutOf))
        autograderResults.write("............................................\n")
        testPoints[testNum]=temp
    
    simpleGrade=True
    scores={}
    Prompt=0
    if io.PromptGrade > 0:
        pp=sum(promptPoints)
        if pp>=io.NumberOfRegularTests: Prompt = io.PromptGrade
        else: Prompt = (io.PromptGrade * sum(promptPoints)) / io.NumberOfRegularTests
        autograderResults.write("Prompt - %.3f out of %s\n"%( Prompt, io.PromptGrade ))
    
    if io.JsonStyle==0:
        total=Prompt
    if io.JsonStyle==1 or io.JsonStyle==2:
        total=0
        if io.PromptGrade > 0:
            scores["Prompt"]=Prompt

    if io.JsonStyle==0 or io.JsonStyle==1:
        total+=sum(testPoints[:io.NumberOfRegularTests])
        scores["Total"]=total
        if len(testPoints[io.NumberOfRegularTests:])>0:
            ectotal=sum(testPoints[io.NumberOfRegularTests:])
            scores["Extra Credit"]=ectotal

    if io.JsonStyle==2:   
        for i in range(1,TotalNumTests+1):
            scores["test%i"%i]=testPoints[i-1]
    
    JSONscores= {'scores':scores}

    autograderResults.write('\n\n======== RESULTS ========\n')
    autograderResults.write(json.dumps(JSONscores))

    autograderResults.close()
    if printResults: print(open(autograderResults.name).read())
    return

def getStudentPromptAndOutputPerTest(output,testNum):
    # Split and clean MIPS results
    try: StudentPrompt=output[testNum*3].strip()
    except: StudentPrompt = "<NO PROMPT FOUND>"
    try: StudentOutput=output[(testNum*3)+1]
    except: StudentOutput = "<NO OUTPUT FOUND>"
    
    StudentPrompt=StudentPrompt.replace('\n','\n   ')
    while '\n\n' in StudentOutput: StudentOutput = StudentOutput.replace('\n\n','\n')
    StudentOutput = [r.strip() for r in StudentOutput.split('\n')]
    return StudentOutput,StudentPrompt

def generateInput():
    global io
    if not(io.RequiresUserInput): return ""
    lines=list(io.getAllUserInputLines())

    if len(lines)>0: 
        lines.append("YOU SHOULD NOT BE ABLE TO SEE THIS")
        inputFile = open(localDir + 'input.txt','w')
        inputFile.writelines('\n'.join(lines))
        inputFile.writelines('\n')
        inputFile.close()
        return " < %sinput.txt "%localDir
    
    return ""

def mips(concatFile= "concat.s"):
    global io,outputFile
    subprocess.call("echo \"\" > %s"%outputFile, shell=True)
    subprocess.call("echo \"\" > %serror.txt"%localDir, shell=True)
    

    userInput = generateInput()
    
    if io.BareMode: BareMode = "-bare "
    else: BareMode = ""
    errorpath=localDir+'error.txt'
    if concatFile == "concat.s": concatpath=localDir+'concat.s'
    else: concatpath = concatFile
    instruction="spim {baremode} -file {concat} {userinput} >> {output} 2>> {error}".format(
        baremode=BareMode,
        concat=concatpath,    error=errorpath,
        userinput=userInput,  output=outputFile
    )
    try:
        subprocess.call(instruction,shell=True,timeout=3)
    except subprocess.TimeoutExpired: 
        return '    Your Program Timed Out due to an infinite loop in MIPS'
    except:
        return "    UH-OH your program failed to run for an unknown reason"
    return ""
    
def GetMipsOutput():
    global outputFile
    NoneAsciiMSG=""
    try:
        with open(outputFile,mode='r' ) as f: output=f.read()
    except:
        with open(outputFile,mode='rb') as f: output=f.read()

        probIndices=reversed([(m.start(0),m.end(0)) for m in re.finditer(bytes('[^\x00-\x7F]+','utf-8'),output)])
        for (s,e) in probIndices:
            asc=hex(int.from_bytes(output[s:e],"big"))
            output=output[:s]+bytes('<NON ASCII DATA>( %s )'%asc,'utf-8')+output[e:]

        NoneAsciiMSG = "non ascii characters were printed"
        #output=re.sub(bytes('[^\x00-\x7F]+','utf-8'),bytes('<NON ASCII DATA>','utf-8'), output)
        output=output.decode('utf-8','replace')
        with open(localDir + 'output2.txt',mode='w') as f: f.write(output)
    output = output.split('\nXXFFVV3793\n')

    output=[o.strip() for o in output]
    
    header_error=output.pop(0)
    header_error=header_error.split('\n',6)     # a JAL instruction is missing a corresponding label
    header_error=header_error[6].strip() if len(header_error)>=6 else ""
    
    return output,header_error,NoneAsciiMSG

def PrintMipsError(headerErr, lastOutput, SPIMerror, NonAsciiMSG,completionErr,runMips):
    autograderResults.write("\nthe following errors occurred\n")
    autograderResults.write("=============================\n")
    allErrors=""
    # errors/Warnings that occurred while concatenating the submission
    with open(localDir + 'concatErrors.txt', 'r') as f:  
        concatErr = f.read().strip()
    if len(concatErr)>0: 
        allErrors+=concatErr+"\n\n"

    # States that the program terminated early
    if len(completionErr)>0: 
        allErrors+=completionErr+"\n\n"

    # SPIM was force quit due to infinite loop
    if len(SPIMerror)>0: 
        allErrors+=SPIMerror+"\n\n" 

    # problem occurred while reading output such as non ascii data
    if len(NonAsciiMSG)>0: 
        allErrors+=NonAsciiMSG+"\n\n"

    # prints out the MIPS HEADER section excluding The emulator header - will be empty if ran successfully
    if len(headerErr)>0: 
        allErrors+=headerErr.strip()+"\n\n"
    
    # Any errors generated by while running mips program such as syntax errors etc
    if(runMips):
        with open(localDir + 'error.txt', 'r') as f:  
            MIPSerr = f.read().strip()
    else: MIPSerr = "program was never run due to potential illegal syscalls"
    if len(MIPSerr)>0:  allErrors += "runtime error:\n   %s\n"%MIPSerr
    if ("Attempt to execute non-instruction" in MIPSerr):
        allErrors += "   ^^^ Your subroutine must terminate with a JUMP RETURN\n\n"
    elif len(MIPSerr)>0: allErrors+='\n'

    # prints out the last section of mips output will be empty if ran successfully
    if len(lastOutput)>0: allErrors+=lastOutput.strip() + "\n\n" 
    
    if len(allErrors)>0: 
        autograderResults.write(allErrors.strip())
    else: 
        autograderResults.write("    None\n")
    autograderResults.write("=============================\n\n")


def ShowInput(test):
    PrintMemInputs(test)
    PrintRegInputs(test)
    printUserInput(test)
    print('\n')

def ShowOutput(test,StudentOutput,StudentPrompt):
    PrintStudentPrompt(StudentPrompt)
    printOutput(test,StudentOutput, True)

def ShowAll(test,StudentOutput,StudentPrompt):
    PrintMemInputs(test)
    PrintRegInputs(test)
    PrintStudentPrompt(StudentPrompt)
    printUserInput(test)
    printOutput(test,StudentOutput, True)



        

def ShowDetails(testNum,test:Test,StudentOutput,StudentPrompt=None):
    global io
    autograderResults.write("TEST %i "%(testNum))
    
    if test.ExtraCredit: autograderResults.write( '(Extra Credit) ')
    T=test.ShowLevel
    I=io.ShowLevel
    if test.ShowLevel == Show.NONE: return

    if io.ShowLevel==Show.ALL: autograderResults.write("=========== test%i ==========\n"%testNum)
    else: autograderResults.write("\nSample Output\n==============\n")

    if test.ShowLevel==Show.INPUT:
        autograderResults.write("(Input Only)\n")
        ShowInput(test)
    
    if test.ShowLevel==Show.OUTPUT:
        autograderResults.write("(Output Only)\n")
        ShowOutput(test,StudentOutput, StudentPrompt)
    
    if test.ShowLevel==Show.ALL:
        ShowAll(test,StudentOutput,StudentPrompt)

    autograderResults.write("TEST %i"%(testNum))


def PrintMemInputs(test):    
    if len(test.MemInputs)>0: autograderResults.write("\nInitial Data in Memory -->\n")   
    for inp in test.MemInputs:
        autograderResults.write("   addr(%s) =  %s \"%s\""%(inp.addr,inp.type,inp.data))

def PrintRegInputs(test):
    if len(test.RegInputs): autograderResults.write("\nRegister Input Values -->\n")   
    for inp in test.RegInputs:
        val = GetHexAndDecOrString(inp.value)
        autograderResults.write("   reg: %s = %s\n"%(inp.reg,val))

def PrintStudentPrompt(StudentPrompt):
    if StudentPrompt != None:
        autograderResults.write("\nYour Prompt -->\n")
        if len(StudentPrompt.strip())<2: 
            autograderResults.write("   <NO PROMPT WAS FOUND>\n")
        else: 
            autograderResults.write("   %s\n"%StudentPrompt)

def printUserInput(test):
    fl = test.UserInput
    if len(fl)>0: autograderResults.write("\nUser Input -->\n")   
    for line in fl:
        autograderResults.write("   %s\n"%line)

def printOutput(test,StudentOutput, _printHeader):    
    if _printHeader: 
        autograderResults.write("\nOutput -->\n")
    for i, Eoutput in enumerate(test.Output):
        if Eoutput.addr is None:
            ExAns = GetHexAndDecOrString(test.ExpectedAnswers[i], int(Eoutput.type))
            autograderResults.write(" Expected   %s = %s\n"%(Eoutput.reg,ExAns))
            try:
                studentAns = GetHexAndDecOrString(StudentOutput[i],int(Eoutput.type))
                autograderResults.write("   Actual   %s = %s\n\n"%(Eoutput.reg,studentAns))

            except:
                try: 
                    StudentOutput[i] # test for value before printing anything
                    autograderResults.write("   <FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT>\n")
                    autograderResults.write(StudentOutput[i])
                except:
                    if ("<NO OUTPUT FOUND>") in StudentOutput:
                        autograderResults.write("   Actual   %s = %s\n\n"%(Eoutput.reg,studentAns))
                    else:
                        autograderResults.write(StudentOutput)
            continue
        else: 
            autograderResults.write(" Expected   %s at address %s\n"%(test.ExpectedAnswers[i],Eoutput.addr))
            try:
                r=StudentOutput[i]
                if len(r.strip())==0:
                    r = "NO STRING WAS FOUND" 
                autograderResults.write("   Actual   %s at address %s\n\n"%(r,Eoutput.addr))
            except:
                try: 
                    StudentOutput[i] # test for value before printing anything
                    autograderResults.write("   FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT\n")
                    autograderResults.write(StudentOutput[i])
                except: 
                    if ("<NO OUTPUT FOUND>") in StudentOutput:
                        autograderResults.write("   Actual   %s at address %s\n\n"%(r,Eoutput.addr))
                    else:
                        autograderResults.write(StudentOutput)
            continue

def Is_int(s):
    try:
        int(s)
        return True
    except: return False

def to_hex(val, nbits=32):
    val=int(val)
    return hex((val + (1 << nbits)) % (1 << nbits))

def GetHexAndDecOrString(s, type=0):
    s=s.strip()
    if type == 11 and len(s)==1:  return " %s ( \'%s\' )"%(to_hex(ord(s)),s)

    if Is_int(s): return "%s ( %s )"%(s, to_hex(s))
    
    if s[0:1] == '0x': return "%s ( %i )"%(int(s[2:],16), s)
    
    return s


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=Show.NONE # overrides json "show" and shows the StudentOutputs of every test

    autograder(_ShowAll=_ShowAll)
                                                                                                                                                                                                         grader/template/                                                                                    0000755 0001750 0001750 00000000000 14044051443 013416  5                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 grader/template/TemplateInitRegister                                                                0000644 0001750 0001750 00000000067 14033650266 017456  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 
lui <reg>, <upper_val>
addi <reg>, <reg>, <lower_val>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         grader/template/TemplateStaticTrailer                                                               0000644 0001750 0001750 00000001301 14044051443 017602  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 
.text
zzzneaten:
	sw $a0, 0($sp)
	sw $v0, 4($sp)
	sw $ra, 8($sp)
	addi $sp, $sp, -12

	lui $a0, 0x9000		
	addi $a0,$a0,0x0230
	addi $v0, $0, 4		
	syscall
	
	addi $sp, $sp, 12
	lw $a0, 0($sp)
	lw $v0, 4($sp)
	lw $ra, 8($sp)

	jr $ra
	add $0,$0,$0

zzzdivider:
	sw $a0, 0($sp)
	sw $v0, 4($sp)
	sw $ra, 8($sp)
	addi $sp, $sp, -12

	jal zzzneaten

	lui $a0, 0x9000		
	addi $a0,$a0,0x0220
	addi $v0, $0, 4		
	syscall

	jal zzzneaten

	addi $sp, $sp, 12
	lw $a0, 0($sp)
	lw $v0, 4($sp)
	lw $ra, 8($sp)

	jr $ra
	add $0,$0,$0
	
main:
	<TRIALS>
	
	addi $v0, $0, 10
	syscall
#________________________
# Subroutine Code 
# Begins Here
#vvvvvvvvvvvvvvvvvvvvvvvv
                                                                                                                                                                                                                                                                                                                               grader/template/TemplateInitMemory                                                                  0000644 0001750 0001750 00000000041 14043335314 017125  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 
.data <addr>
	<type> <data>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   grader/template/TemplateTrial                                                                       0000644 0001750 0001750 00000000413 14044051443 016106  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 
# ============================
# <TEST NAME>    <TEST NUMBER>

	jal zzzdivider
	add $0, $0, $0

	<inputs>

	jal <student_subroutine>
	add $0,$0,$0

	jal zzzdivider
	add $0, $0, $0

	#add $t0, $0, $a0
	#add $t1, $0, $v0

	<outputs>


	jal zzzdivider
	add $0, $0, $0

                                                                                                                                                                                                                                                     grader/template/TemplateOut                                                                         0000644 0001750 0001750 00000000245 14033650266 015613  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 
sw $a0, 0($sp)
sw $v0, 4($sp)

lui <lui_reg>, <upper_addr>
addi $a0, <reg>, <lower_addr>
addi $v0, $0, <type>
syscall

jal zzzneaten

lw $a0, 0($sp)
lw $v0, 4($sp)
                                                                                                                                                                                                                                                                                                                                                           grader/template/TemplateStaticHeader                                                                0000644 0001750 0001750 00000000111 14044051443 017366  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 
.kdata 0x90000220
	.asciiz "XXFFVV3793"
.kdata 0x90000230
	.asciiz "\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                       grader/settings.py                                                                                  0000644 0001750 0001750 00000021543 14044072556 014032  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 import json,os,sys,random
from enum import Enum

class Show(Enum):
    NONE=0
    INPUT=1
    OUTPUT=2
    ALL=3

    def __gt__(self,other): return self.value>other.value
    def __ge__(self,other): return self.value>=other.value
    def __lt__(self,other): return self.value<other.value
    def __le__(self,other): return self.value<=other.value


#TODO MAX points need to account for individual tests
#TODO Prompt Points must ignore extra credit
#TODO seperate Regular Tests and extra credit Tests
class settings():


    def __init__(self, file=None,**kwargs):
        if file is None:
            self.empty(**kwargs)
            return

        with open(file, 'r') as f: io = json.load(f)
        self.io=io

        self.SubroutineName=io["subroutine_name"]
        
        self.PromptGrade=float(io.get("PromptGrade",0))
        self.TestGrade=float(io.get("TestGrade",1))
        self.ECTestGrade=float(io.get("ECTestGrade",self.TestGrade))
        self.ShowLevel=Show(io.get("ShowLevel",0))
        self.MessageToStudent=io.get("MessageToStudent","")
        self.BareMode = io.get("BareMode",False)
        self.Shuffle = io.get("Shuffle",False)
        self.JsonStyle = io.get("JsonStyle",0)
        self.RequiresUserInput = io.get("RequiresUserInput",False)
        
        if type(self.BareMode) is str: self.BareMode = self.BareMode.lower()=="true"
        if type(self.Shuffle)  is str: self.Shuffle  = self.Shuffle.lower() =="true"
        if type(self.RequiresUserInput) is str: self.RequiresUserInput = self.RequiresUserInput.lower()=="true"
        
        self.NumberOfRegularTests=0
        self.AllTests=self.CreateTests(io["tests"],io,canShuffle=True)


    def empty(self,**kwargs):
        self.io=None
        self.SubroutineName=None
        self.PromptGrade=None
        self.TestGrade=None
        self.ECTestGrade=None
        self.MessageToStudent=None
        self.ShowLevel=Show.NONE
        self.BareMode = False
        self.RequiresUserInput = False
        self.AllTests=[]

    def CreateTests(self,alltests_json,io,canShuffle=False):
        reg,ec=[],[]
        for i,testjs in enumerate(alltests_json):
            test=Test(parent=self,testjs=testjs,testNumber=i)
            if test.ExtraCredit: ec.append(test)
            else:                reg.append(test)
        if self.Shuffle and canShuffle:
            random.shuffle(ec)
            random.shuffle(reg)
        self.NumberOfRegularTests=len(reg)
        return reg+ec

    def getAllUserInputLines(self):
        for test in self.AllTests:
            for line in test.UserInput:
                yield line

    def printHeader(self):
        print("\n\nREQUIRED ROUTINE: %s"%self.SubroutineName)
        if self.MessageToStudent:
            print("GENERAL MESSAGE: %s\n"%self.MessageToStudent)
    def ToDict(self):
        io={}
        io["subroutine_name"]=self.SubroutineName
        io["PromptGrade"]=self.PromptGrade
        io["TestGrade"]=self.TestGrade
        io["ECTestGrade"]=self.ECTestGrade
        io["MessageToStudent"]=self.MessageToStudent
        io["BareMode"]=self.BareMode
        io["RequiresUserInput"]=self.RequiresUserInput
        io["ShowLevel"]=self.ShowLevel.value
        io["Shuffle"]=self.Shuffle
        io["JsonStyle"]=self.JsonStyle
        io["tests"]=[t.ToDict() for t in self.AllTests]
        return io

class Test():
    parent:settings
    # Initialize from JSON
    def __init__(self,parent, testjs=None,testNumber=0,**kwargs):
        self.parent=parent
        if testjs is None: 
            self.empty(**kwargs)
            return

        self.ShowLevel =  max(Show(testjs.get("ShowLevel",0)) , parent.ShowLevel )
        self.testName   = testjs.get("name","Test").strip()
        self.testNumber = testNumber   
        self.ExtraCredit= testjs.get("ExtraCredit",False) 
        self.OutOf      = testjs.get("OutOf",0) or (parent.ECTestGrade if self.ExtraCredit else parent.TestGrade)
        self.UserInput  = testjs.get("UserInput",[])
        
        if type(self.ExtraCredit) is str: self.ExtraCredit= self.ExtraCredit.lower()=="true"
        
        # Get Inputs and Outputs
        self.MemInputs,self.RegInputs = self.setInputs(testjs.get("inputs",[]))
        self.ExpectedAnswers,self.Output=self.setOutputs(testjs["outputs"])
        i=0
    def empty(self,**kwargs):
        self.testName = "Test"
    
        self.ExtraCredit = False
        self.ShowLevel=Show.NONE
        self.OutOf = 0
        self.UserInput = []

        self.MemInputs=[]
        self.RegInputs=[]
        self.Output=[]
    
    def ToDict(self):
        testjs={}
        testjs["name"]=self.testName
        testjs["ExtraCredit"]=self.ExtraCredit 
        if self.OutOf==(self.parent.ECTestGrade if self.ExtraCredit else self.parent.TestGrade):
            testjs["OutOf"]=0
        else: testjs["OutOf"]=self.OutOf 
        testjs["ShowLevel"]=Show.NONE.value if self.ShowLevel == self.parent.ShowLevel else self.ShowLevel.value
        testjs["UserInput"]=self.UserInput
        testjs["inputs"]=[i.ToDict() for i in self.MemInputs]
        testjs["inputs"] += [i.ToDict() for i in self.RegInputs if not i.memPointer]
        testjs["outputs"]=[i.ToDict() for i in self.Output]
        return testjs
        
    def setInputs(self, inputs):
        memInputs=[]
        regInputs=[]
        for inp in inputs:

            try: 
                memInputs.append( self.__MemInput__( inp["addr"], inp["data"],inp["type"]))
                try: 
                    memInputs[-1].reg=inp["reg"]
                    regInputs.append( self.__RegInput__( inp["reg"], inp["addr"],memPointer=True))
                except KeyError as e:pass #print(e)
            except KeyError: None

            try: regInputs.append( self.__RegInput__( inp["reg"], inp["value"]))
            except KeyError: None
        return memInputs,regInputs

    def setOutputs(self, outputsJS):
        ExpectedAnswers=[]
        outputs=[]
        for out in outputsJS:
            ans=out["CorrectAnswer"]
            ExpectedAnswers.append(ans)
            try: # print string stored at address out["addr"] 
                outputs.append( self.__Output__( type='4', reg='a0', addr=out["addr"],CorrectAnswer=ans))
                continue
            except KeyError as e: pass#print(e) 
        
            try: # print value of register
                outputs.append( self.__Output__(  type=out["type"], reg=out["reg"],CorrectAnswer=ans))
            except:  raise Exception("Output not address or register")
        return ExpectedAnswers,outputs

            
    class __RegInput__:
        def __init__(self,reg,value,memPointer=False):
            self.reg='$'+reg.replace('$','')
            self.value=value
            self.memPointer=memPointer
        
        def ToDict(self):
            if self.memPointer is False: 
                return {"reg":self.reg.replace("$",""),"value":self.value}

    class __MemInput__:
        def __init__(self,addr,data,type,reg=None):
            self.addr=addr
            self.data=data
            self.type=type
            self.reg=reg
            
            if "ascii" in type.lower(): 
                self.data=self.data.replace("\\\"","quote_7654123")
                self.data=self.data.replace("\"","")
                self.data=self.data.replace("quote_7654123","\\\"")
                self.data='\"'+self.data+'\"'

        
        def ToDict(self):
            d = { "type":self.type, "addr":self.addr, 'data':self.data.replace("\"","") }
            if self.reg is not None: d["reg"]=self.reg.replace("$","")
            return d
    
    class __Output__:
        def __init__(self,type,CorrectAnswer,reg=None,addr=None):
            if reg is None and addr is None: raise Exception("reg or addr must be given a value")
            if reg is not None: self.reg = '$'+reg.replace('$','')
            else:self.reg=reg
            self.type = str(type)
            self.addr = addr
            self.CorrectAnswer = CorrectAnswer
            
            if addr is None:
                self.lui_reg = "$0"
                self.upper_addr = '0'
                self.lower_addr = '0'
            else:
                if reg is not None: self.lui_reg = '$'+reg.replace('$','')
                if '0x' in addr.strip(): 
                    addr = addr.strip()[2:].zfill(8)
                self.upper_addr = '0x'+addr[:4]
                self.lower_addr = '0x'+addr[4:]
        
        def ToDict(self):
            d = {"type":self.type, "CorrectAnswer":self.CorrectAnswer }
            if self.addr is not None: d["addr"]=self.addr
            if self.reg is not None: d["reg"]=self.reg.replace("$","")
            return d
                

def isInt(val):
    try:
        float(val)
        return True
    except:
        return False


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    tt = settings("settings.json")
    d=tt.ToDict()
    j=json.dumps(d,indent=4)
    print(j)



            


                                                                                                                                                             grader/__init__.py                                                                                  0000644 0001750 0001750 00000000206 14044060145 013711  0                                                                                                    ustar   kamian                          kamian                                                                                                                                                                                                                 from .autograder import autograder
from .concat import concat
from .settings import settings,Test,Show
from .wrapper import runGrader
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          