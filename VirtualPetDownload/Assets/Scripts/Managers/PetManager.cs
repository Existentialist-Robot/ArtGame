using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PetManager : MonoBehaviour
{
    public Animator petAnim;
    public PetController pet;
    public NeedsController needsController;
    public float petMoveTimer, originalpetMoveTimer;
    public Transform[] waypoints;
    public GameObject gameOver;
    public Text gameOverText;

    public static PetManager instance;

    private void Awake()
    {
       // needsController.Initialize(100, 100, 100, 15, 5, 7);
        originalpetMoveTimer = petMoveTimer;
        gameOver.SetActive(false);
        if (instance == null)
        {
            instance = this;
        }
        else Debug.LogWarning("More than one PetManager in the Scene");
    }

    private void Update()
    {
        if (petMoveTimer > 0)
        {
            petMoveTimer -= Time.deltaTime;
        }
        else
        {
            MovePetToRandomWaypoint();
            petMoveTimer = originalpetMoveTimer;
        }
    }

    private void MovePetToRandomWaypoint()
    {
        int randomWaypoint = Random.Range(0, waypoints.Length);
        pet.Move(waypoints[randomWaypoint].position);
    }

    public void Die()
    {
        petAnim.SetTrigger("died");
        gameOver.SetActive(true);
        gameOverText.text = "She Just Died.";


    }
    public void RestartGame()
    {
        gameOver.SetActive(false);
        pet.Fine();
        needsController.Initialize(100,100,100,15,5,7);
    }
}
