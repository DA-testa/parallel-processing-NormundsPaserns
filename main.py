# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    current_time = 0
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    for job_index, processing_time in enumerate(data):
        if threads:
            processing_start_time, thread_index = heapq.heappop(threads)
            output.append((thread_index, processing_start_time))
            processing_end_time = processing_start_time + processing_time
            heapq.heappush(threads, (processing_end_time, thread_index))
        else:
            processing_start_time, thread_index = heapq.heappop(threads)
            current_time = processing_start_time
            output.append((thread_index, processing_start_time))
            processing_end_time = processing_start_time + processing_time
            heapq.heappush(threads, (processing_end_time, thread_index))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, processing_start_time in result:
        print(thread_index, processing_start_time)

if __name__ == "__main__":
    main()
