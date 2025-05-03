# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Good Data Visualization: Florence Nightingale's Rose Diagram
Why it's classified as good:
Florence Nightingale's Rose Diagram (also known as the Coxcomb chart) created in 1858 is considered an excellent example of data visualization for several reasons that align with principles covered in our course materials.
First, the visualization excels in its substantive qualities by accurately and honestly representing mortality data from the Crimean War. Nightingale meticulously collected data on soldier deaths, categorizing them by cause (disease, wounds, or other causes), and represented this information with mathematical precision using her innovative circular diagram. The visualization clearly communicated that preventable diseases were causing far more deaths than battlefield wounds, which aligned with the actual data rather than preconceived notions.
Second, the visualization demonstrates strong perceptual qualities through its innovative design. As discussed in our course materials, choosing the right visualization for your data is crucial. Nightingale's circular design with uniform angular sections and varying radii effectively communicated both seasonal patterns and the relative magnitude of different causes of death. The use of color coding (blue for disease, red for wounds, black for other causes) created immediate visual distinction between categories, allowing viewers to quickly grasp the key message without requiring extensive statistical knowledge.
Third, the diagram exemplifies aesthetic qualities through its clean, organized design. Despite being created in the 1850s, it follows many modern design principles we've studied, including clear labeling, appropriate use of color to differentiate categories, and a layout that draws attention to the most important information. The circular format effectively displays cyclical time data while the proportional areas communicate magnitude, creating a visually appealing yet informative graphic.
Finally, this visualization demonstrates excellent advocacy qualities, aligning with our discussion of data visualization as advocacy. Nightingale used this graphic not merely to display data but to advocate for sanitary reforms in military hospitals. Her diagram was persuasive because it employed what the course identified as rational appeal (presenting clear facts), moral appeal (showing preventable deaths), and emotional appeal (visualizing the scale of unnecessary suffering).
How it could be improved:
While Nightingale's Rose Diagram was revolutionary for its time and remains influential today, there are several ways it could be improved using modern data visualization principles:
First, the visualization could benefit from improved accessibility considerations. As discussed in our course materials on accessible data visualization, the original reliance solely on color to distinguish categories (blue, red, and black) might create difficulties for viewers with color vision deficiencies. A modern version could incorporate additional visual cues such as patterns or textures to ensure all viewers can distinguish between categories, following the principle that we shouldn't rely solely on color to convey critical information.
Second, the diagram could be enhanced through interactive elements to improve user engagement and exploration. As we learned in the section on advanced visualization techniques, interactive features such as tooltips displaying exact values, the ability to filter data by time period or cause, or zoom functionality would allow viewers to explore the data more deeply while maintaining the powerful visual impact of the original.
Third, modern annotation techniques could be incorporated to guide viewers through the key insights. Following principles from our customizing plots lesson, strategic text annotations could highlight critical patterns, explain methodology, or provide context about historical events that influenced the data, helping viewers better understand both the visualization and its implications.
These improvements would maintain the integrity and impact of Nightingale's groundbreaking work while leveraging modern techniques to enhance its effectiveness for contemporary audiences.

Bad Data Visualization: Fox News Tax Rate Bar Chart
Why it's classified as bad:
The Fox News bar chart comparing tax rates (showing a comparison between the "Now" rate of 35% and "Jan 1, 2013" rate of 39.6%) exemplifies several problematic data visualization practices we've studied in this course.
The most significant issue with this visualization is its misleading substantive qualities through the intentional manipulation of the y-axis. As emphasized in our course materials on choosing the right visualization, bar charts must use a zero baseline because they represent quantitative values through the length of bars. By starting the y-axis at 34% instead of 0%, this visualization dramatically exaggerates the proportional difference between the two values. The visual difference appears to be 460% larger, making what is actually a 13.1% increase look like a massive jump. This violates the fundamental principle that data visualizations should honestly represent the underlying data.
Second, the chart demonstrates poor perceptual qualities through its cluttered design and unclear labeling. Our lessons on effective visualization emphasized the importance of clear labels and minimal chart junk. This visualization contains unnecessary visual elements such as gridlines and decorative borders that distract from the data itself. Additionally, the y-axis is unlabeled and placed on the right side of the chart where it is less likely to be noticed, further obscuring the manipulation.
Third, the visualization fails in terms of accessibility considerations. The small text size of the axis values makes the chart difficult to read, and the placement of critical information in non-standard locations (such as the y-axis on the right) creates additional cognitive load for viewers. As we learned in our lesson on accessible visualization, good data visualization should minimize cognitive barriers to understanding.
This example perfectly illustrates what D'Ignazio and Klein described in our readings about data visualization as rhetorical objects. While all visualizations make choices about how to represent reality, this example crosses the line into deliberate misrepresentation by using design choices that lead viewers to dramatically incorrect conclusions about the magnitude of the tax rate change.
How it could be improved:
This visualization could be substantially improved by applying several principles from our course:
First and most importantly, the y-axis should start at zero to accurately represent the proportional difference between the values. As emphasized in our lessons on perceptual qualities of data visualization, bar charts must use a zero baseline to ensure that the visual representation aligns with the actual data. This single change would transform a misleading visualization into an honest one.
Second, the visual clutter should be reduced following Edward Tufte's concept of the data-ink ratio that we discussed in class. Removing unnecessary gridlines, borders, and decorative elements would create a cleaner visualization that focuses viewer attention on the actual data rather than distractions.
Third, proper labeling should be implemented to provide complete context. The y-axis should be clearly labeled (e.g., "Tax Rate (%)"), placed in the standard left position, and include a full range of values. Clear titles and annotations could also provide additional context about the significance of the tax rate change.
Fourth, an alternative visualization might be more appropriate. If the goal is to show the relative impact of a tax increase, other visualization types such as a line chart showing the trend over time or a unit chart showing the dollar impact on different income levels might better communicate the actual significance of the change without misleading viewers.






      
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 30/04/2025`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
