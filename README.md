

```
docker build -t registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-armafira/ir-datasets:0.0.3 .
```

```
docker push registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-armafira/ir-datasets:0.0.3
```



```
tira-run \
    --output-directory ${PWD}/iranthology-dataset-tira \
    --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-armafira/ir-datasets:0.0.3 \
    --allow-network true \
    --command '/irds_cli.sh --ir_datasets_id iranthology-ArMaFiRa --output_dataset_path $outputDir'
```

