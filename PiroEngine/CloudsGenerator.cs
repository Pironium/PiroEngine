using System.Collections.Generic;
using UnityEngine;

public class CloudsGenerator : MonoBehaviour
{
    public GameObject cloudPrefab;
    public int numberOfClouds = 10;
    public Vector3 cloudSpawnArea = new Vector3(100, 20, 100);

    private List<GameObject> clouds = new List<GameObject>();

    void Start()
    {
        GenerateClouds();
    }

    void GenerateClouds()
    {
        for (int i = 0; i < numberOfClouds; i++)
        {
            Vector3 randomPosition = new Vector3(
                Random.Range(-cloudSpawnArea.x, cloudSpawnArea.x),
                Random.Range(cloudSpawnArea.y / 2, cloudSpawnArea.y),
                Random.Range(-cloudSpawnArea.z, cloudSpawnArea.z)
            );

            GameObject newCloud = Instantiate(cloudPrefab, randomPosition, Quaternion.identity);
            clouds.Add(newCloud);
        }
    }

    void Update()
    {
        // Move clouds slowly over time
        foreach (var cloud in clouds)
        {
            cloud.transform.Translate(Vector3.right * Time.deltaTime);
        }
    }
}
