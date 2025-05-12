# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  

- For each visualization, describe and justify: 
# Assignment 3: Final Project
## Data Visualization of Toronto Dog Bite Incidents

For this assignment, I analyzed a dataset from the City of Toronto's Open Data Portal related to dog bite incidents. This dataset provides information about reported dog bite incidents in Toronto, including breed information, bite severity, and other relevant details.

## Dataset Source
Toronto Dog Bite Incidents dataset from the City of Toronto's Open Data Portal
https://www.toronto.ca/city-government/data-research-maps/open-data/

## Visualizations Created

I created two distinct visualizations from this dataset:

1. **Python Visualization**: A multi-dimensional scatter plot showing the relationship between dog breed bite frequency, severity, and overall risk assessment.

2. **Excel Visualization**: A horizontal stacked bar chart comparing bite severity distributions across different dog breed groups.

Each visualization addresses different aspects of the dataset and uses different approaches to communicate information about dog bite risks in Toronto.

The detailed analysis of each visualization can be found in the following documents:
- [Python Visualization Analysis](python-visualization.md)
- [Excel Visualization Analysis](excel-visualization.md)

## Appendix: Code

The complete Python code used for data analysis and visualization is included in the `dogbiteanalysis.py` file. Key components include:

1. Data loading and cleaning
2. Statistical analysis of breed vs. severity relationships
3. Creation of breed groups for more meaningful analysis
4. Risk score calculation combining frequency and severity metrics
5. Generation of multiple visualizations including the scatter plot discussed in the analysis

For the Excel visualization, the data processing steps included:
1. Importing the CSV data into Excel
2. Creating breed groups using VLOOKUP and nested IF functions
3. Creating pivot tables to summarize the data by breed group and severity
4. Calculating percentage metrics using array formulas
5. Creating and formatting the stacked bar chart with appropriate color coding and direct labeling

   Python: 

For this visualization, I used Python with libraries including Pandas, Matplotlib, and Seaborn. The scatter plot combines multiple variables through point position, size, and color to create a comprehensive risk assessment visualization of dog breeds involved in bite incidents.
Intended Audience
The primary audience for this visualization is Toronto public health officials, animal control departments, and policymakers who need data-driven insights to inform dog bite prevention strategies and public safety policies. Secondary audiences include dog owners, animal rescue organizations, and the general public interested in understanding dog bite risks in their community.
Information and Message
This scatter plot conveys a multi-dimensional analysis of dog bite risk factors by combining:

Incident frequency (x-axis): The total number of reported bites for each breed
Bite severity (y-axis): The percentage of bites classified as "severe" or "very severe"
Computed risk score (bubble size): A combined metric that multiplies frequency by severity percentage
Severity percentage (color gradient): Reinforcing the severity dimension through color

The visualization allows viewers to quickly identify which breeds represent the highest overall risk to public safety by considering both how often they bite and how severe those bites tend to be. The quadrant annotations help categorize breeds into risk profiles (high frequency/high severity being the highest concern).
Design Considerations
Several design principles were applied to enhance the effectiveness of this visualization:

Data-ink ratio: The visualization maximizes information density by encoding four variables (frequency, severity, risk score, breed name) in a single plot without unnecessary decoration.
Color encoding: A sequential "YlOrRd" (yellow-orange-red) color scheme provides intuitive severity indication, with darker red representing higher severity.
Reference lines: Dotted reference lines showing averages help viewers quickly evaluate each breed relative to overall norms.
Quadrant labeling: Text annotations clearly divide the plot into meaningful risk categories.
Direct labeling: Each data point is directly labeled with its breed name, eliminating the need for a separate legend that would require eye movement between the data and the key.
Multi-level legends: Clear legends for both the size encoding (risk score) and color encoding (severity) provide necessary context.

Reproducibility
I ensured reproducibility through several practices:

Fully scripted workflow: The entire data pipeline from loading to visualization is contained in a Python script with no manual steps.
Version control: The code is maintained in a GitHub repository, allowing others to reproduce the exact visualization.
Dependency management: All required libraries are explicitly imported at the beginning of the script.
Random seed control: When applicable, random seed values are set to ensure consistent results.
Detailed commenting: The code includes explanatory comments about data transformation and visualization choices.
Parameter documentation: Key parameters like color schemes and sizing factors are clearly defined and explained.

Accessibility
The visualization incorporates several accessibility features:

Color and redundant encoding: Information is conveyed through multiple channels (position, size, AND color), ensuring colorblind users can still interpret the data.
Text contrast: All text labels use high-contrast backgrounds to ensure readability.
Clear annotations: Quadrant labels and data point labels are designed with sufficient size and contrast.
Alternative text: The figure includes descriptive alt-text when published digitally.
High resolution: The image is saved at 300 DPI to ensure clarity when printed or viewed on different devices.
Multiple visual cues: Reference lines and annotations provide context through different visual channels.

Impacted Communities
This visualization potentially impacts several communities:

Dog owners: Particularly owners of breeds identified as high-risk, who may face increased scrutiny or regulations.
Breed-specific communities: Groups advocating for specific breeds (especially those often subject to breed-specific legislation) may be affected by how their preferred breeds are represented.
Public health officials: Those responsible for creating bite prevention programs or policies may base decisions on this visualization.
Vulnerable populations: Children and elderly persons who are disproportionately affected by severe dog bites benefit from improved risk awareness.
Animal shelter workers: Those making adoption decisions or implementing safety protocols based on breed-specific risk levels.

I carefully considered potential biases and stigmatization when creating this visualization, ensuring that it presents objective data while acknowledging that breed is just one factor in dog bite incidents.
Feature Selection
From the available dataset, I made deliberate choices about which features to include or exclude:

Included features:

Breed (categorical): Essential for the breed-specific risk analysis
Bite circumstance (categorical): Used to categorize severity levels
Incident count (numerical): Basic frequency measure
Severity percentage (derived): Calculated to show proportion of severe incidents


Excluded features:

Geographic information: While potentially valuable, would have overcomplicated this specific visualization
Temporal data: Seasonal patterns were analyzed separately
Dog size/weight: Not consistently available in the dataset
Victim demographics: Important but better addressed in a separate visualization



These choices were made to maintain focus on the core question: which breeds present the greatest combined risk based on both bite frequency and severity?
Underwater Labor
Creating this visualization required substantial "underwater labor" that isn't immediately apparent:

Data cleaning: Extensive work to standardize breed names and merge similar breeds (e.g., "GERM SHEPHERD" and "GERM SHEPHERD MIX").
Missing data handling: Developing strategies for incidents with incomplete information.
Severity classification: Creating a meaningful severity scale based on raw "Bite_Circumstance" categories.
Risk score development: Experimentation with different mathematical approaches to combining frequency and severity.
Statistical validation: Performing Chi-square tests to validate relationships between breeds and severity.
Visualization iterations: Multiple iterations testing different encodings, scales, and annotations before arriving at the final version.



Excel:

For this visualization, I used Microsoft Excel to create a horizontal stacked bar chart that shows the distribution of bite severity categories across different dog breed groups. Excel was chosen as it's widely accessible to various stakeholders and allows for straightforward data manipulation before visualization.
Intended Audience
This visualization targets animal control officers, veterinarians, and municipal policymakers who need clear, actionable information about which breed groups represent higher risks for severe bites. The simplified presentation also makes it accessible to the general public who may be seeking to understand relative risks associated with different types of dogs.
Information and Message
The visualization communicates the proportion of different bite severity levels across major dog breed groups in Toronto. By displaying both the count (bar length) and percentage (labeled at end of bars) of severe incidents for each breed group, the chart allows viewers to understand:

Which breed groups have the highest absolute numbers of reported bites
Which breed groups have the highest proportion of severe/very severe bites
How the severity distribution varies between different breed groups

The core message is that certain breed groups (particularly "Working Dogs" and "Terrier Types") have not only high bite frequencies but also disproportionately high percentages of severe bites, suggesting these groups may warrant special consideration in prevention strategies.
Design Considerations
I applied several design principles when creating this visualization:

Hierarchical organization: Breed groups are sorted by total incidents, allowing viewers to quickly identify the most commonly reported groups.
Color coding: I used a consistent color scheme where red tones represent severe bites, green represents non-severe bites, and blue represents incidents classified as "not a bite," creating an intuitive severity scale.
Direct labeling: Percentage labels are placed directly at the end of bars, eliminating the need for viewers to estimate values or refer to a separate legend.
Horizontal orientation: Using a horizontal rather than vertical bar chart accommodates breed group labels without requiring awkward text rotation.
Clear legend: The stacked bar segments are clearly identified in a legend that uses both color and text to ensure clarity.
Limited clutter: Grid lines and other non-essential elements were minimized to maintain focus on the data.
Consistent formatting: Text sizes, colors, and styling were kept consistent throughout to create a cohesive visual presentation.

Reproducibility
While Excel visualizations are sometimes criticized for reproducibility challenges, I took several steps to ensure this visualization can be recreated:

Documented data source: The visualization draws from a clearly identified public dataset (Toronto's dog bite data) available through the Open Data Portal.
Saved template: The Excel file includes both raw data and the visualization with all formatting preserved.
Formula documentation: All calculations (such as percentage of severe bites) are documented within the spreadsheet using cell comments.
Named ranges: Key data elements are defined as named ranges to improve formula readability and reusability.
No manual adjustments: All visual elements are generated through Excel's formatting tools rather than custom manual adjustments.

However, Excel's workflow does introduce reproducibility limitations compared to the Python visualization, as it involves more manual steps and potential for inconsistency if the process is repeated.
Accessibility
I incorporated several accessibility features into the Excel visualization:

High contrast colors: The color scheme was selected to maintain sufficient contrast between adjacent segments and against the background.
Pattern fills: In addition to color, different bar segments use pattern fills (solid, striped, etc.) to ensure distinguishability for colorblind users.
Direct labels: Key percentages are directly labeled, reducing reliance on visual estimation.
Alt text: When saved as an image or embedded in documents, descriptive alt text is included.
Simple font choices: Sans-serif fonts with appropriate sizing ensure readability across different display environments.
Printable design: The visualization remains effective when printed in grayscale by maintaining distinguishable patterns.

Impacted Communities
This visualization may impact several communities:

Dog owners: Particularly those who own breeds categorized in the higher-risk groups, who may face increased scrutiny or feel unfairly stereotyped.
Breed advocacy groups: Organizations working to change public perception of certain breeds may be concerned about reinforcing negative stereotypes.
Public health professionals: Those developing bite prevention programs may use this data to allocate resources.
Insurance companies: May use such data to inform policy decisions regarding coverage for certain breeds.
Animal shelters: Staff who make adoption recommendations based partly on public safety considerations.

I sought to present the data objectively while being sensitive to the fact that breed alone is not deterministic of bite risk, and individual dog behavior varies significantly within breed groups.
Feature Selection
I made deliberate choices about which aspects of the dataset to include in this visualization:

Included features:

Breed groups rather than individual breeds: This simplified the visualization while highlighting meaningful patterns
Four severity categories: Maintained the full range of bite classifications to provide nuanced understanding
Both absolute counts and percentages: Allowed viewers to assess both overall volume and relative severity


Excluded features:

Demographic information about bite victims: While important, this would have complicated the visualization and shifted focus
Temporal trends: While the dataset contained time information, including it would have required a different visualization type
Geographic distribution: Spatial patterns are significant but better addressed in a separate map-based visualization
Individual incident details: These would overwhelm the visualization without adding meaningful pattern information



These choices focused the visualization on the core relationship between breed groups and bite severity while maintaining interpretability.
Underwater Labor
The Excel visualization required significant "underwater labor" that isn't immediately visible in the final product:

Data aggregation: Consolidating individual breeds into meaningful groups required domain knowledge about canine classifications.
Data cleaning: Addressing inconsistencies in breed naming conventions and severity classifications.
Iterative design testing: Multiple versions were created to test different organization methods (sorting by count vs. percentage, experimenting with vertical vs. horizontal orientation).
Color scheme testing: Testing multiple color schemes to ensure both aesthetic appeal and accessibility.
Format optimization: Adjusting text sizes, bar widths, and spacing to balance information density with readability.
Legend placement: Testing different legend placements to minimize eye movement while interpreting the chart.

- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09/05/2025`
* The branch name for your repo should be: `assignment-3`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_3.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
