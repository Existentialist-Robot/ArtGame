using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PetController : MonoBehaviour
{
    public Animator petAnimator;
    private Vector3 destination;
    public float speed;
    public NeedsController needsController;

    private void Awake()
    {
        //needsController.Initialize(100, 100, 100, 15, 5, 7);   
    }

    private void Update()
    {
        if (Vector3.Distance(transform.position,destination) > 0.5f)
        {
            transform.position = Vector3.MoveTowards(transform.position,destination, speed*Time.deltaTime);
        }
    }

    public void Move(Vector3 destination)
    {
        this.destination = destination;
    }

    public void Fine()
    {
        petAnimator.SetTrigger("idle");
    }

    public void Happy()
    {
        petAnimator.SetTrigger("Happy");
        petAnimator.ResetTrigger("idle");
    }

    public void Hungry()
    {
        petAnimator.SetTrigger("hungry");
        petAnimator.ResetTrigger("idle");
    }

    public void Sad()
    {
        petAnimator.SetTrigger("antsy");
        petAnimator.ResetTrigger("idle");
    }

    public void Tired()
    {
        petAnimator.SetTrigger("tired");
        petAnimator.ResetTrigger("idle");
    }

    public void Eat()
    {
        petAnimator.SetTrigger("eat");
        petAnimator.ResetTrigger("idle");
    }
    public void Drug()
    {
        petAnimator.SetTrigger("drug");
        petAnimator.ResetTrigger("idle");
    }
    public void Netflix()
    {
        petAnimator.SetTrigger("netflix");
        petAnimator.ResetTrigger("idle");
    }
}
