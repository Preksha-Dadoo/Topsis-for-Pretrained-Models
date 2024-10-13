print("TOPSIS Scores:", topsis_score)
print("Rankings:", rankings)

model_names = ['Model A', 'Model B', 'Model C']

plt.figure(figsize=(10, 6))
plt.barh(model_names, topsis_score, color='skyblue')
plt.xlabel('TOPSIS Score')
plt.title('TOPSIS Scores of Sports Text Summarization Models')
plt.xlim(0, 1)  
plt.grid(axis='x', linestyle='--', alpha=0.7)

for index, value in enumerate(topsis_score):
    plt.text(value + 0.02, index, f'Rank: {rankings[index]}', va='center')

plt.tight_layout()
plt.show()
