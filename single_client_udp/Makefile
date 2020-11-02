all: setup p1

setup:
	rm -f nagle_ack_log.txt

p1:
	python3 tcp_client.py 0 0 & python3 tcp_server.py 0 0

clean_nagle:
	rm -f nagle_ack_log.txt

clean_best_nagle:
	rm -f nagle_ack_log_best_buffer.txt

clean_buffer:
	rm -f diff_buffer_log.txt
	rm -f diff_buffer/*

difference:
	python3 find_diff.py

wc:
	python3 find_wc.py

clean_difference:
	rm -f difference_files/*

clean_wc:
	rm -f wc_log.txt