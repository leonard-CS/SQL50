import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['machine_id', 'process_id'], inplace=True)
    durations = []
    for _, group in activity.groupby(['machine_id', 'process_id']):
        start_time = group[group['activity_type'] == 'start']['timestamp'].values[0]
        end_time = group[group['activity_type'] == 'end']['timestamp'].values[0]
        durations.append({'machine_id': group['machine_id'].values[0], 'duration': end_time - start_time})
    durations_df = pd.DataFrame(durations)
    avg_durations = durations_df.groupby('machine_id')['duration'].mean().reset_index()
    avg_durations.rename(columns={'duration': 'processing_time'}, inplace=True)
    avg_durations['processing_time'] = avg_durations['processing_time'].round(3)
    return avg_durations

if __name__ == '__main__':
    data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
    activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})

    result = get_average_time(activity)
    print(result)
