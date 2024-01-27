FROM ros:humble

COPY rosnode /node
COPY entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh

WORKDIR /node

RUN colcon build

# "/bin/entrypoint.sh", "ros2", "run", "rosnode", "pubsub"
CMD [ "/bin/entrypoint.sh" ]
