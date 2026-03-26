
mkdir -p results

CONTAINER_NAME="customer-container"

echo "Copying output files from container:"

docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt results/ 2>/dev/null && echo "Copied insight1.txt" || echo "insight1.txt not found"
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt results/ 2>/dev/null && echo "Copied insight2.txt" || echo "insight2.txt not found"
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt results/ 2>/dev/null && echo "Copied insight3.txt" || echo "insight3.txt not found"
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png results/ 2>/dev/null && echo "Copied summary_plot.png" || echo "summary_plot.png not found"
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt results/ 2>/dev/null && echo "Copied clusters.txt" || echo "clusters.txt not found"
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv results/ 2>/dev/null && echo "Copied data_preprocessed.csv" || echo "data_preprocessed.csv not found"
docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv results/ 2>/dev/null && echo "Copied data_raw.csv" || echo "data_raw.csv not found"

echo "Stopping and removing container :"

docker stop $CONTAINER_NAME 2>/dev/null && echo "Container stopped" || echo "Container not running"
docker rm $CONTAINER_NAME 2>/dev/null && echo "Container removed" || echo "Container not found"

echo "done"