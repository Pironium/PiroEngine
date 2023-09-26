using System.Collections.Generic;
using UnityEngine;

public class BezierSplineSmoothing
{
    public static List<Vector3> SmoothBezierSpline(List<Vector3> controlPoints, int segments)
    {
        List<Vector3> smoothedPoints = new List<Vector3>();
        
        for (int i = 0; i < controlPoints.Count - 3; i += 3)
        {
            for (int j = 0; j <= segments; j++)
            {
                float t = j / (float)segments;
                float u = 1 - t;
                float tt = t * t;
                float uu = u * u;
                float uuu = uu * u;
                float ttt = tt * t;
                
                Vector3 p = uuu * controlPoints[i]
                          + 3 * uu * t * controlPoints[i + 1]
                          + 3 * u * tt * controlPoints[i + 2]
                          + ttt * controlPoints[i + 3];
                          
                smoothedPoints.Add(p);
            }
        }
        
        return smoothedPoints;
    }
}
