# Phase Relationships in the AI Regulation Process

This repository contains the scripts and the data to produce the chart in the "Phase 
Relationships in the AI Regulation Process" article. 

The suggested sequence is as follows:
1. Download scientific paper counts from Arxiv.org with arxiv-monthly.py script:

```bash
python arxiv-monthly.py > cs.ai.submissions.monthly.csv
```

2. Download Google Trends histories for terms "AI regulation" and "Responsible AI" using these 
links:
https://trends.google.com/trends/explore?date=all&q=AI%20Regulation&hl=en
https://trends.google.com/trends/explore?date=all&q=Responsible%20AI&hl=en
and rename the results to ai_regulation.csv and responsible_ai.csv
(or simply use my versions)

3. Launch iPython Notebook file ai-phases.ipynb and execute it to the chart. 

Feel free to use in any way you want, any feedback is appreciated!
	 
