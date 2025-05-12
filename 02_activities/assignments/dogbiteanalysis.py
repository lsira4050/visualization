# Dog Breed vs. Bite Severity Analysis
# This script focuses specifically on analyzing the relationship between 
# dog breeds and bite severity in the Toronto dog bite dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Set the style for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('muted')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Define colors for consistency - NAB category removed
severity_colors = {
    'VERY SEVERE': '#d32f2f',
    'SEVERE': '#f44336',
    'NON SEVERE': '#4caf50',
    'NOT A BITE': '#2196f3'
}

def analyze_breed_severity(csv_file):
    """
    Analyze the relationship between dog breeds and bite severity
    
    Parameters:
    -----------
    csv_file : str
        Path to the CSV file containing the dog bite data
    """
    print(f"Loading data from {csv_file}...")
    
    # Load the data
    df = pd.read_csv(csv_file)
    
    print(f"Dataset contains {len(df)} incidents")
    
    # Filter out NAB category 
    df = df[df['Bite_Circumstance'] != 'NAB'].copy()
    print(f"Dataset after removing NAB category: {len(df)} incidents")
    
    # Create a binary indicator for severe bites (SEVERE or VERY SEVERE)
    df['Severe_Bite'] = df['Bite_Circumstance'].apply(
        lambda x: 1 if x in ['SEVERE', 'VERY SEVERE'] else 0
    )
    
    # 1. Basic Statistics on Bite Severity
    bite_counts = df['Bite_Circumstance'].value_counts()
    bite_percent = df['Bite_Circumstance'].value_counts(normalize=True) * 100
    
    print("\nBite severity distribution:")
    for circumstance, count in bite_counts.items():
        print(f"{circumstance}: {count} ({bite_percent[circumstance]:.2f}%)")
    
    # 2. Breed Analysis
    breed_counts = df['Breed'].value_counts()
    print(f"\nTotal number of unique breeds: {len(breed_counts)}")
    
    # Get top 15 breeds by incident count
    top_breeds = breed_counts.head(15)
    print("\nTop 15 breeds by incident count:")
    for breed, count in top_breeds.items():
        print(f"{breed}: {count} ({count/len(df)*100:.2f}%)")
    
    # 3. Create cross-tabulation of breed vs. bite severity for top breeds
    top_breeds_list = top_breeds.index.tolist()
    breed_filter = df['Breed'].isin(top_breeds_list)
    breed_severity = pd.crosstab(df[breed_filter]['Breed'], df[breed_filter]['Bite_Circumstance'])
    
    # Ensure all severity columns exist - NAB removed
    for severity in ['VERY SEVERE', 'SEVERE', 'NON SEVERE', 'NOT A BITE']:
        if severity not in breed_severity.columns:
            breed_severity[severity] = 0
    
    # Calculate total incidents per breed
    breed_severity['Total'] = breed_severity.sum(axis=1)
    
    # Calculate percentage of severe/very severe bites
    if 'VERY SEVERE' in breed_severity.columns:
        breed_severity['Severe_Pct'] = (breed_severity['SEVERE'] + breed_severity['VERY SEVERE']) / breed_severity['Total'] * 100
    else:
        breed_severity['Severe_Pct'] = breed_severity['SEVERE'] / breed_severity['Total'] * 100
    
    # Sort by severity percentage
    breed_severity_by_pct = breed_severity.sort_values('Severe_Pct', ascending=False)
    
    print("\nBreed vs. Bite Severity (sorted by % severe/very severe):")
    for breed, row in breed_severity_by_pct.iterrows():
        severe_count = row.get('VERY SEVERE', 0) + row['SEVERE']
        print(f"{breed}: {severe_count}/{row['Total']} severe incidents ({row['Severe_Pct']:.1f}%)")
    
    # 4. Group similar breeds together for better analysis
    # Define breed groups
    breed_groups = {
        "Shepherd Types": ["GERM SHEPHERD", "GERM SHEPHERD MIX", "DUTCH SHEPHERD", "BELGIAN MALINOIS"],
        "Bulldog Types": ["AMER BULLDOG", "AMER BULLDOG MIX", "ENG BULLDOG", "FRENCH BULLDOG", "AM PIT BULL TER / ENG BULLDOG"],
        "Retriever Types": ["LABRADOR RETR", "GOLDEN RETR", "LABRADOR RETR MIX", "GOLDEN RETR MIX"],
        "Terrier Types": ["AM PIT BULL TER", "YORKSHIRE TERR", "JACK RUSSELL TER", "TERRIER MIX"],
        "Working Dogs": ["ROTTWEILER", "AKITA", "DOBERMAN PINSC", "CANE CORSO", "BOXER"],
        "Huskies/Nordic": ["SIBERIAN HUSKY", "ALASKAN MALAMUTE", "HUSKY MIX"],
        "Small Breeds": ["CHIHUAHUA", "SHIH TZU", "DACHSHUND", "PUG", "BEAGLE", "POMERANIAN"],
        "Other/Mixed": []  # Will catch all others
    }
    
    # Function to find the group for a breed
    def find_breed_group(breed):
        for group, breeds in breed_groups.items():
            if any(b in breed for b in breeds):
                return group
        return "Other/Mixed"
    
    # Add a 'Breed_Group' column to the dataframe
    df['Breed_Group'] = df['Breed'].apply(find_breed_group)
    
    # Create a cross-tabulation by breed group
    group_severity = pd.crosstab(df['Breed_Group'], df['Bite_Circumstance'])
    
    # Ensure all severity columns exist - NAB removed
    for severity in ['VERY SEVERE', 'SEVERE', 'NON SEVERE', 'NOT A BITE']:
        if severity not in group_severity.columns:
            group_severity[severity] = 0
    
    # Calculate totals and percentages
    group_severity['Total'] = group_severity.sum(axis=1)
    if 'VERY SEVERE' in group_severity.columns:
        group_severity['Severe_Pct'] = (group_severity['SEVERE'] + group_severity['VERY SEVERE']) / group_severity['Total'] * 100
    else:
        group_severity['Severe_Pct'] = group_severity['SEVERE'] / group_severity['Total'] * 100
    
    # Sort by total number of incidents
    group_severity_by_total = group_severity.sort_values('Total', ascending=False)
    
    print("\nBreed Group Analysis:")
    for group, row in group_severity_by_total.iterrows():
        severe_count = row.get('VERY SEVERE', 0) + row['SEVERE']
        print(f"{group}: {severe_count}/{row['Total']} severe incidents ({row['Severe_Pct']:.1f}%)")
    
    # 5. Statistical Analysis: Chi-Square Test for relationship between breed group and severity
    # Create a contingency table of breed group vs. severe/not severe
    contingency_table = pd.crosstab(df['Breed_Group'], df['Severe_Bite'])
    
    # Perform chi-square test
    from scipy.stats import chi2_contingency
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    print(f"\nChi-Square Test for Breed Group vs. Severity:")
    print(f"Chi2 value: {chi2:.2f}")
    print(f"p-value: {p:.4f}")
    print(f"Degrees of freedom: {dof}")
    if p < 0.05:
        print("Result: There is a statistically significant association between breed group and bite severity.")
    else:
        print("Result: There is not enough evidence to suggest an association between breed group and bite severity.")
    
    # 6. Risk Assessment: Combine frequency and severity
    # Create a dataframe with breed, total incidents, and severe percentage
    breed_risk = pd.DataFrame({
        'Breed': top_breeds.index,
        'Total_Incidents': top_breeds.values,
        'Severe_Pct': [breed_severity.loc[breed, 'Severe_Pct'] for breed in top_breeds.index]
    })
    
    # Calculate a risk score (arbitrary formula: incidents * severity_percentage / 100)
    breed_risk['Risk_Score'] = breed_risk['Total_Incidents'] * breed_risk['Severe_Pct'] / 100
    breed_risk = breed_risk.sort_values('Risk_Score', ascending=False)
    
    print("\nBreed Risk Assessment (combining incident frequency and severity):")
    for _, row in breed_risk.iterrows():
        print(f"{row['Breed']}: {row['Total_Incidents']} incidents, {row['Severe_Pct']:.1f}% severe, Risk Score: {row['Risk_Score']:.1f}")
    
    # 7. Visualizations
    print("\nGenerating visualizations...")
    
    # 7.1 Pie chart of bite severity with improved legend
    plt.figure(figsize=(10, 8))
    wedges, texts, autotexts = plt.pie(
        bite_counts, 
        labels=None,  # No direct labels on pie chart for cleaner look
        autopct='%1.1f%%', 
        startangle=90, 
        colors=[severity_colors.get(circ, '#999999') for circ in bite_counts.index]
    )
    
    # Add a clear legend with labels
    plt.legend(
        wedges, 
        bite_counts.index,
        title="Bite Severity",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=12
    )
    
    # Enhance text appearance
    for autotext in autotexts:
        autotext.set_fontsize(11)
        autotext.set_weight('bold')
    
    plt.axis('equal')
    plt.title('Distribution of Bite Severity (n={})'.format(len(df)), fontsize=16)
    plt.tight_layout()
    plt.savefig('bite_severity_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7.2 Bar chart of breeds by severe percentage with improved legend - FIXED
    plt.figure(figsize=(12, 8))
    
    # Create custom color map for better visualization
    custom_cmap = sns.color_palette("YlOrRd", n_colors=len(breed_severity_by_pct))
    
    ax = sns.barplot(
        x=breed_severity_by_pct['Severe_Pct'], 
        y=breed_severity_by_pct.index,
        palette=custom_cmap
    )
    
    # Add percentage labels to bars
    for i, v in enumerate(breed_severity_by_pct['Severe_Pct']):
        ax.text(v + 1, i, f"{v:.1f}%", va='center', fontweight='bold')
    
    # Remove the colorbar code that was causing the error
    # Instead, add a text annotation explaining the color gradient
    plt.text(
        0.98, 0.02, 'Colors represent severity percentage (darker = higher)',
        transform=plt.gca().transAxes,
        ha='right', va='bottom',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7)
    )
    
    plt.xlabel('Percentage of Severe/Very Severe Bites', fontsize=14)
    plt.ylabel('Dog Breed', fontsize=14)
    plt.title('Top Breeds by Severe/Very Severe Bite Percentage', fontsize=16)
    plt.xlim(0, 100)
    plt.tight_layout()
    plt.savefig('breeds_by_severity_percentage.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7.3 Stacked bar chart of breed groups by bite severity with improved legend
    severe_cols = [col for col in ['VERY SEVERE', 'SEVERE', 'NON SEVERE', 'NOT A BITE'] 
                  if col in group_severity.columns]
    group_severity_plot = group_severity[severe_cols].copy()
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot stacked bars
    group_severity_plot.plot(
        kind='bar', 
        stacked=True,
        figsize=(14, 8),
        color=[severity_colors.get(col, '#999999') for col in severe_cols],
        ax=ax
    )
    
    # Improve legend appearance
    legend = plt.legend(
        title='Bite Severity',
        title_fontsize=14,
        fontsize=12,
        loc='upper right', 
        bbox_to_anchor=(1.15, 1)
    )
    
    # Add percentage labels for severe/very severe
    for i, v in enumerate(group_severity['Severe_Pct']):
        ax.text(i, group_severity['Total'][i] + 2, f"{v:.1f}%", ha='center', fontweight='bold')
    
    plt.title('Breed Groups by Bite Severity', fontsize=16)
    plt.xlabel('Breed Group', fontsize=14)
    plt.ylabel('Number of Incidents', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('breed_groups_by_severity.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7.4 Advanced visualization: Scatter plot of breed risk with improved legend
    plt.figure(figsize=(14, 10))
    
    # Create the scatter plot
    scatter = plt.scatter(
        breed_risk['Total_Incidents'],
        breed_risk['Severe_Pct'],
        s=breed_risk['Risk_Score'] * 20,  # Size based on risk score
        c=breed_risk['Severe_Pct'],  # Color based on severity
        cmap='YlOrRd',
        alpha=0.7
    )
    
    # Add breed labels to each point
    for _, row in breed_risk.iterrows():
        plt.annotate(
            row['Breed'],
            (row['Total_Incidents'], row['Severe_Pct']),
            fontsize=9,
            ha='center',
            va='bottom',
            xytext=(0, 5),
            textcoords='offset points'
        )
    
    # Add reference lines
    plt.axhline(y=breed_risk['Severe_Pct'].mean(), color='gray', linestyle='--', alpha=0.5,
               label=f'Avg Severity: {breed_risk["Severe_Pct"].mean():.1f}%')
    plt.axvline(x=breed_risk['Total_Incidents'].mean(), color='gray', linestyle='--', alpha=0.5,
               label=f'Avg Incidents: {breed_risk["Total_Incidents"].mean():.1f}')
    
    # Add colorbar with clear label
    cbar = plt.colorbar(scatter)
    cbar.set_label('Severity Percentage (%)', fontsize=12)
    
    # Add size legend for risk score
    from matplotlib.lines import Line2D
    
    # Create custom legend elements for size
    size_legend_elements = [
        Line2D([0], [0], marker='o', color='w', 
               markerfacecolor='#ff7f0e', markersize=8,
               label='Risk Score: 5'),
        Line2D([0], [0], marker='o', color='w', 
               markerfacecolor='#ff7f0e', markersize=12,
               label='Risk Score: 15'),
        Line2D([0], [0], marker='o', color='w', 
               markerfacecolor='#ff7f0e', markersize=16,
               label='Risk Score: 30')
    ]
    
    # Create a custom legend for reference lines
    ref_legend_elements = [
        Line2D([0], [0], color='gray', lw=2, linestyle='--', alpha=0.5,
              label=f'Avg Severity: {breed_risk["Severe_Pct"].mean():.1f}%'),
        Line2D([0], [0], color='gray', lw=2, linestyle='--', alpha=0.5,
              label=f'Avg Incidents: {breed_risk["Total_Incidents"].mean():.1f}')
    ]
    
    # Place both legends
    size_legend = plt.legend(handles=size_legend_elements, loc='lower right', 
                        title='Risk Score (Bubble Size)', frameon=True)
    plt.gca().add_artist(size_legend)  # Add the first legend
    
    plt.legend(handles=ref_legend_elements, loc='upper right', frameon=True)
    
    # Customize the plot
    plt.title('Dog Breed Risk Assessment: Incident Frequency vs. Severity', fontsize=16)
    plt.xlabel('Number of Incidents', fontsize=14)
    plt.ylabel('Percentage of Severe/Very Severe Bites', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    # Add annotations for quadrants
    plt.text(
        0.95, 0.95, 'High Severity, Low Frequency',
        transform=plt.gca().transAxes,
        ha='right', va='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7)
    )
    plt.text(
        0.95, 0.05, 'Low Severity, Low Frequency',
        transform=plt.gca().transAxes,
        ha='right', va='bottom',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7)
    )
    plt.text(
        0.05, 0.95, 'High Severity, High Frequency',
        transform=plt.gca().transAxes,
        ha='left', va='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7)
    )
    plt.text(
        0.05, 0.05, 'Low Severity, High Frequency',
        transform=plt.gca().transAxes,
        ha='left', va='bottom',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7)
    )
    
    plt.tight_layout()
    plt.savefig('breed_risk_assessment_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7.5 Heatmap of breeds vs. bite circumstances with improved legend
    # Focus on the top 15 breeds
    top15_severity = breed_severity.loc[top_breeds.index]
    
    # Get just the severity columns (not the calculated columns)
    severity_cols = [col for col in ['VERY SEVERE', 'SEVERE', 'NON SEVERE', 'NOT A BITE'] 
                    if col in top15_severity.columns]
    
    # Create a normalized version (percentage within each breed)
    normalized_severity = top15_severity[severity_cols].div(top15_severity['Total'], axis=0) * 100
    
    # Create the heatmap with improved legend
    plt.figure(figsize=(12, 10))
    ax = sns.heatmap(
        normalized_severity,
        annot=True,
        fmt='.1f',
        cmap='YlOrRd',
        linewidths=.5,
        cbar_kws={
            'label': 'Percentage within Breed (%)',
            'shrink': 0.8
        }
    )
    
    # Customize colorbar
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label('Percentage within Breed (%)', fontsize=14)
    
    plt.title('Bite Severity Distribution by Breed (Percentage)', fontsize=16)
    plt.ylabel('Dog Breed', fontsize=14)
    plt.xlabel('Bite Circumstance', fontsize=14)
    plt.tight_layout()
    plt.savefig('breed_severity_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 8. Summary of findings
    print("\nSummary of Key Findings:")
    print(f"- Total analyzed incidents: {len(df)}")
    print(f"- Overall percentage of severe/very severe bites: {df['Severe_Bite'].mean()*100:.1f}%")
    
    # Breeds with highest severity (>75%)
    high_severity_breeds = breed_severity[breed_severity['Severe_Pct'] > 75].index.tolist()
    print("\nBreeds with highest severity percentage (>75%):")
    for breed in high_severity_breeds:
        print(f"- {breed}: {breed_severity.loc[breed, 'Severe_Pct']:.1f}%")
    
    # Breed groups by severity
    print("\nBreed group severity percentages (highest to lowest):")
    for group, row in group_severity.sort_values('Severe_Pct', ascending=False).iterrows():
        print(f"- {group}: {row['Severe_Pct']:.1f}%")
    
    # Top 5 breeds by risk score
    print("\nTop 5 breeds by combined risk score:")
    for _, row in breed_risk.head(5).iterrows():
        print(f"- {row['Breed']}: {row['Risk_Score']:.1f} risk score")
    
    print("\nVisualization files created:")
    print("1. bite_severity_distribution.png - Pie chart of bite severity distribution")
    print("2. breeds_by_severity_percentage.png - Bar chart of breeds by severity percentage")
    print("3. breed_groups_by_severity.png - Stacked bar chart of breed groups by severity")
    print("4. breed_risk_assessment_scatter.png - Scatter plot of frequency vs. severity")
    print("5. breed_severity_heatmap.png - Heatmap of severity distribution by breed")
    
    print("\nAnalysis complete!")
    return df, breed_severity, group_severity, breed_risk

if __name__ == "__main__":
    # Run the analysis
    df, breed_severity, group_severity, breed_risk = analyze_breed_severity('Ddogs.csv')